/* SPDX-License-Identifier: ISC */
/*
 * Authors: Dan Williams
 *          Martin Lucina
 *          Ricardo Koller
 *          Felipe Huici <felipe.huici@neclab.eu>
 *          Florian Schmidt <florian.schmidt@neclab.eu>
 *          Simon Kuenzer <simon.kuenzer@neclab.eu>
 *
 * Copyright (c) 2015-2017 IBM
 * Copyright (c) 2016-2017 Docker, Inc.
 * Copyright (c) 2017 NEC Europe Ltd., NEC Corporation
 *
 * Permission to use, copy, modify, and/or distribute this software
 * for any purpose with or without fee is hereby granted, provided
 * that the above copyright notice and this permission notice appear
 * in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL
 * WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
 * AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
 * CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
 * OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
 * NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
 * CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */

#include <string.h>
#include <uk/plat/common/sections.h>
#include <x86/cpu.h>
#include <x86/traps.h>
#include <kvm/config.h>
#include <kvm/console.h>
#include <kvm/intctrl.h>
#include <kvm-x86/multiboot.h>
#include <kvm-x86/multiboot_defs.h>
#include <uk/arch/limits.h>
#include <uk/arch/types.h>
#include <uk/plat/console.h>
#include <uk/assert.h>
#include <uk/essentials.h>
#include <x86/acpi/acpi.h>
#include <uk/swrand.h>

#define PLATFORM_MEM_START 0x100000
#define PLATFORM_MAX_MEM_ADDR 0x40000000

#define MAX_CMDLINE_SIZE 8192
static char cmdline[MAX_CMDLINE_SIZE];

struct kvmplat_config _libkvmplat_cfg = { 0 };

extern void _libkvmplat_newstack(uintptr_t stack_start, void (*tramp)(void *),
				 void *arg);

static inline void _mb_get_cmdline(struct multiboot_info *mi)
{
	char *mi_cmdline;

	if (mi->flags & MULTIBOOT_INFO_CMDLINE) {
		mi_cmdline = (char *)(__u64)mi->cmdline;

		if (strlen(mi_cmdline) > sizeof(cmdline) - 1)
			uk_pr_err("Command line too long, truncated\n");
		strncpy(cmdline, mi_cmdline,
			sizeof(cmdline));
	} else {
		/* Use image name as cmdline to provide argv[0] */
		uk_pr_debug("No command line present\n");
		strncpy(cmdline, CONFIG_UK_NAME, sizeof(cmdline));
	}

	/* ensure null termination */
	cmdline[(sizeof(cmdline) - 1)] = '\0';
}

static inline void _mb_init_mem(struct multiboot_info *mi)
{
	multiboot_memory_map_t *m;
	size_t offset, max_addr;

	/*
	 * Look for the first chunk of memory at PLATFORM_MEM_START.
	 */
	for (offset = 0; offset < mi->mmap_length;
	     offset += m->size + sizeof(m->size)) {
		m = (void *)(__uptr)(mi->mmap_addr + offset);
		if (m->addr == PLATFORM_MEM_START
		    && m->type == MULTIBOOT_MEMORY_AVAILABLE) {
			break;
		}
	}
	UK_ASSERT(offset < mi->mmap_length);

	/*
	 * Cap our memory size to PLATFORM_MAX_MEM_SIZE which boot.S defines
	 * page tables for.
	 */
	max_addr = m->addr + m->len;
	if (max_addr > PLATFORM_MAX_MEM_ADDR)
		max_addr = PLATFORM_MAX_MEM_ADDR;
	UK_ASSERT((size_t) __END <= max_addr);

	/*
	 * Reserve space for boot stack at the end of found memory
	 */
	if ((max_addr - m->addr) < __STACK_SIZE)
		UK_CRASH("Not enough memory to allocate boot stack\n");
	
#ifdef CONFIG_RUNTIME_ASLR
	int ASLR_offset;
	int divisor = 1;
	/*
	 * Since we can't modify __STACK_SIZE which is a macro, we place first the 
	 * stack and then the heap. 
	 * //TODO Discuss and add a limiting factor to the offset
	 */
	ASLR_offset = uk_swrand_randr() % (max_addr/4);
	_libkvmplat_cfg.bstack.end = ALIGN_UP(max_addr - ASLR_offset, __PAGE_SIZE);
	_libkvmplat_cfg.bstack.start   = _libkvmplat_cfg.bstack.end-__STACK_SIZE;
	_libkvmplat_cfg.bstack.len   = __STACK_SIZE;

	uk_pr_info(" ASLR - Stack : s: %p e: %p\n",_libkvmplat_cfg.bstack.start,
	_libkvmplat_cfg.bstack.end);
	
	do{
	ASLR_offset = uk_swrand_randr() % (max_addr/(4*divisor));
	_libkvmplat_cfg.heap.start = ALIGN_UP((uintptr_t) __END+ASLR_offset, __PAGE_SIZE);
	divisor++;
	}
	while(_libkvmplat_cfg.heap.start >= _libkvmplat_cfg.bstack.start);
	
	divisor = 1;
	
	do{
	ASLR_offset = uk_swrand_randr() % (max_addr/(8*divisor));
	_libkvmplat_cfg.heap.end = (uintptr_t) _libkvmplat_cfg.bstack.start-ASLR_offset;
	divisor++;
	}
	while(_libkvmplat_cfg.heap.end >= _libkvmplat_cfg.bstack.start);
	
	_libkvmplat_cfg.heap.len   = _libkvmplat_cfg.heap.end
				     - _libkvmplat_cfg.heap.start;
	uk_pr_info(" ASLR - Heap : s: %p e: %p len: %p\n",_libkvmplat_cfg.heap.start,
	_libkvmplat_cfg.heap.end,_libkvmplat_cfg.heap.len );
				 
#else
	_libkvmplat_cfg.heap.start = ALIGN_UP((uintptr_t) __END, __PAGE_SIZE);
	_libkvmplat_cfg.heap.end   = (uintptr_t) max_addr - __STACK_SIZE;
	_libkvmplat_cfg.heap.len   = _libkvmplat_cfg.heap.end
				     - _libkvmplat_cfg.heap.start;
	_libkvmplat_cfg.bstack.start = _libkvmplat_cfg.heap.end;
	_libkvmplat_cfg.bstack.end   = max_addr;
	_libkvmplat_cfg.bstack.len   = __STACK_SIZE;
#endif
}

static inline void _mb_init_initrd(struct multiboot_info *mi)
{
	multiboot_module_t *mod1;
	uintptr_t heap0_start, heap0_end;
	uintptr_t heap1_start, heap1_end;
	size_t    heap0_len,   heap1_len;

	/*
	 * Search for initrd (called boot module according multiboot)
	 */
	if (mi->mods_count == 0) {
		uk_pr_debug("No initrd present\n");
		goto no_initrd;
	}

	/*
	 * NOTE: We are only taking the first boot module as initrd.
	 *       Initrd arguments and further modules are ignored.
	 */
	UK_ASSERT(mi->mods_addr);

	mod1 = (multiboot_module_t *)((uintptr_t) mi->mods_addr);
	UK_ASSERT(mod1->mod_end >= mod1->mod_start);

	if (mod1->mod_end == mod1->mod_start) {
		uk_pr_debug("Ignoring empty initrd\n");
		goto no_initrd;
	}

	_libkvmplat_cfg.initrd.start = (uintptr_t) mod1->mod_start;
	_libkvmplat_cfg.initrd.end = (uintptr_t) mod1->mod_end;
	_libkvmplat_cfg.initrd.len = (size_t) (mod1->mod_end - mod1->mod_start);

	/*
	 * Check if initrd is part of heap
	 * In such a case, we figure out the remaining pieces as heap
	 */
	if (_libkvmplat_cfg.heap.len == 0) {
		/* We do not have a heap */
		goto out;
	}
	heap0_start = 0;
	heap0_end   = 0;
	heap1_start = 0;
	heap1_end   = 0;
	if (RANGE_OVERLAP(_libkvmplat_cfg.heap.start,
			  _libkvmplat_cfg.heap.len,
			  _libkvmplat_cfg.initrd.start,
			  _libkvmplat_cfg.initrd.len)) {
		if (IN_RANGE(_libkvmplat_cfg.initrd.start,
			     _libkvmplat_cfg.heap.start,
			     _libkvmplat_cfg.heap.len)) {
			/* Start of initrd within heap range;
			 * Use the prepending left piece as heap */
			heap0_start = _libkvmplat_cfg.heap.start;
			heap0_end   = ALIGN_DOWN(_libkvmplat_cfg.initrd.start,
						 __PAGE_SIZE);
		}
		if (IN_RANGE(_libkvmplat_cfg.initrd.start,

			     _libkvmplat_cfg.heap.start,
			     _libkvmplat_cfg.heap.len)) {
			/* End of initrd within heap range;
			 * Use the remaining left piece as heap */
			heap1_start = ALIGN_UP(_libkvmplat_cfg.initrd.end,
					       __PAGE_SIZE);
			heap1_end   = _libkvmplat_cfg.heap.end;
		}
	} else {
		/* Initrd is not overlapping with heap */
		heap0_start = _libkvmplat_cfg.heap.start;
		heap0_end   = _libkvmplat_cfg.heap.end;
	}
	heap0_len = heap0_end - heap0_start;
	heap1_len = heap1_end - heap1_start;

	/*
	 * Update heap regions
	 * We make sure that in we start filling left heap pieces at
	 * `_libkvmplat_cfg.heap`. Any additional piece will then be
	 * placed to `_libkvmplat_cfg.heap2`.
	 */
	if (heap0_len == 0) {
		/* Heap piece 0 is empty, use piece 1 as only */
		if (heap1_len != 0) {
			_libkvmplat_cfg.heap.start = heap1_start;
			_libkvmplat_cfg.heap.end   = heap1_end;
			_libkvmplat_cfg.heap.len   = heap1_len;
		} else {
			_libkvmplat_cfg.heap.start = 0;
			_libkvmplat_cfg.heap.end   = 0;
			_libkvmplat_cfg.heap.len   = 0;
		}
		 _libkvmplat_cfg.heap2.start = 0;
		 _libkvmplat_cfg.heap2.end   = 0;
		 _libkvmplat_cfg.heap2.len   = 0;
	} else {
		/* Heap piece 0 has memory */
		_libkvmplat_cfg.heap.start = heap0_start;
		_libkvmplat_cfg.heap.end   = heap0_end;
		_libkvmplat_cfg.heap.len   = heap0_len;
		if (heap1_len != 0) {
			_libkvmplat_cfg.heap2.start = heap1_start;
			_libkvmplat_cfg.heap2.end   = heap1_end;
			_libkvmplat_cfg.heap2.len   = heap1_len;
		} else {
			_libkvmplat_cfg.heap2.start = 0;
			_libkvmplat_cfg.heap2.end   = 0;
			_libkvmplat_cfg.heap2.len   = 0;
		}
	}

	/*
	 * Double-check that initrd is not overlapping with previously allocated
	 * boot stack. We crash in such a case because we assume that multiboot
	 * places the initrd close to the beginning of the heap region. One need
	 * to assign just more memory in order to avoid this crash.
	 */
	if (RANGE_OVERLAP(_libkvmplat_cfg.heap.start,
			  _libkvmplat_cfg.heap.len,
			  _libkvmplat_cfg.initrd.start,
			  _libkvmplat_cfg.initrd.len))
		UK_CRASH("Not enough space at end of memory for boot stack\n");
out:
	return;

no_initrd:
	_libkvmplat_cfg.initrd.start = 0;
	_libkvmplat_cfg.initrd.end   = 0;
	_libkvmplat_cfg.initrd.len   = 0;
	_libkvmplat_cfg.heap2.start  = 0;
	_libkvmplat_cfg.heap2.end    = 0;
	_libkvmplat_cfg.heap2.len    = 0;
	return;
}

static void _libkvmplat_entry2(void *arg __attribute__((unused)))
{
	ukplat_entry_argp(NULL, cmdline, sizeof(cmdline));
}
__u32 _gen_seed32(){
	__u32 low,high;
	__asm__ __volatile__ ("rdtsc" : "=a" (low), "=d" (high));
	return ((unsigned long long)high << 32) | low;
}
static int uk_swrand_init(void)
{
	unsigned int i;
#ifdef CONFIG_LIBUKSWRAND_CHACHA
	unsigned int seedc = 10;
	__u32 seedv[10];
#else
	unsigned int seedc = 2;
	__u32 seedv[2];
#endif
	uk_pr_info("Initialize random number generator...\n");

	for (i = 0; i < seedc; i++)
		seedv[i] = _gen_seed32();

	uk_swrand_init_r(&uk_swrand_def, seedc, seedv);

	return seedc;
}

void _libkvmplat_entry(void *arg)
{
	struct multiboot_info *mi = (struct multiboot_info *)arg;
	
	_init_cpufeatures();
	_libkvmplat_init_console();
	traps_init();
	intctrl_init();
	/*
	 * ASLR, We need to rebuild stack and heap once they've been built.
	 * This allows to call the randomization functions.
	 */
	uk_swrand_init();
	
	uk_pr_info("Entering from KVM (x86)...\n");
	uk_pr_info("     multiboot: %p\n", mi);
	/*
	 * The multiboot structures may be anywhere in memory, so take a copy of
	 * everything necessary before we initialise memory allocation.
	 */
	
	_mb_get_cmdline(mi);
	_mb_init_mem(mi);
	_mb_init_initrd(mi);
	
	if (_libkvmplat_cfg.initrd.len)
		uk_pr_info("        initrd: %p\n",
			   (void *) _libkvmplat_cfg.initrd.start);
	uk_pr_info("    heap start: %p\n",
		   (void *) _libkvmplat_cfg.heap.start);
	if (_libkvmplat_cfg.heap2.len)
		uk_pr_info(" heap start (2): %p\n",
			   (void *) _libkvmplat_cfg.heap2.start);
	uk_pr_info("     stack top: %p\n",
		   (void *) _libkvmplat_cfg.bstack.start);

	
#ifdef CONFIG_HAVE_SMP
	acpi_init();
#endif /* CONFIG_HAVE_SMP */

#ifdef CONFIG_HAVE_SYSCALL
	_init_syscall();
#endif /* CONFIG_HAVE_SYSCALL */

#if CONFIG_HAVE_X86PKU
	_check_ospke();
#endif /* CONFIG_HAVE_X86PKU */
	
	/*
	 * Switch away from the bootstrap stack as early as possible.
	 */
	
	uk_pr_info("Switch from bootstrap stack to stack @%p\n",
		   (void *) _libkvmplat_cfg.bstack.end);
	_libkvmplat_newstack(_libkvmplat_cfg.bstack.end,
			     _libkvmplat_entry2, 0);
}
