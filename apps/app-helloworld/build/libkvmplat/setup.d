cmd_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/setup.o := ""gcc -nostdlib -U __linux__ -U __FreeBSD__ -U __sun__ -fno-stack-protector -Wall -Wextra -D __Unikraft__ -DUK_CODENAME="Mimas" -DUK_VERSION=0.7 -DUK_FULLVERSION=0.7.0~3e14fc5-custom -fno-tree-sra -fno-split-stack -nostdinc -Os -fno-omit-frame-pointer -flto -fno-PIC -fhosted -ffreestanding -fno-tree-loop-distribute-patterns   -I/home/terrylos/Thesis/apps/app-helloworld/build/include -I/home/terrylos/Thesis/unikraft/arch/x86/x86_64/include -I/home/terrylos/Thesis/unikraft/include -I/home/terrylos/Thesis/unikraft/lib/devfs/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/arch/x86_64 -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/arch/generic -I/home/terrylos/Thesis/unikraft/lib/posix-user/include -I/home/terrylos/Thesis/unikraft/lib/posix-user/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/syscall_shim/include -I/home/terrylos/Thesis/unikraft/lib/ukalloc/include -I/home/terrylos/Thesis/unikraft/lib/ukallocbbuddy/include -I/home/terrylos/Thesis/unikraft/lib/ukargparse/include -I/home/terrylos/Thesis/unikraft/lib/ukboot/include -I/home/terrylos/Thesis/unikraft/lib/ukbus/include -I/home/terrylos/Thesis/unikraft/lib/ukdebug/include -I/home/terrylos/Thesis/unikraft/lib/uklibparam/include -I/home/terrylos/Thesis/unikraft/lib/uksglist/include -I/home/terrylos/Thesis/unikraft/lib/uksp/include -I/home/terrylos/Thesis/unikraft/lib/ukswrand/include -I/home/terrylos/Thesis/unikraft/lib/uktime/include -I/home/terrylos/Thesis/unikraft/lib/uktime/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/uktimeconv/include -I/home/terrylos/Thesis/unikraft/lib/vfscore/include  -I/home/terrylos/Thesis/unikraft/plat/kvm/include -I/home/terrylos/Thesis/unikraft/plat/common/include -I/home/terrylos/Thesis/unikraft/plat/drivers/include   -D__X86_64__ -m64 -mno-red-zone -fno-asynchronous-unwind-tables -fno-reorder-blocks -mtune=generic -DCC_VERSION=12.0 -fno-builtin-printf -fno-builtin-fprintf -fno-builtin-sprintf -fno-builtin-snprintf -fno-builtin-vprintf -fno-builtin-vfprintf -fno-builtin-vsprintf -fno-builtin-vsnprintf -fno-builtin-scanf -fno-builtin-fscanf -fno-builtin-sscanf -fno-builtin-vscanf -fno-builtin-vfscanf -fno-builtin-vsscanf -DCONFIG_UK_NETDEV_SCRATCH_SIZE=0  -DKVMPLAT     -g3 -D__LIBNAME__=libkvmplat -D__BASENAME__=setup.c -c /home/terrylos/Thesis/unikraft/plat/kvm/x86/setup.c -o /home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/setup.o -Wp,-MD,/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/.setup.o.d

source_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/setup.o := /home/terrylos/Thesis/unikraft/plat/kvm/x86/setup.c

deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/setup.o := \
    $(wildcard include/config/memory/dedup/aslr.h) \
    $(wildcard include/config/uk/name.h) \
    $(wildcard include/config/runtime/aslr.h) \
    $(wildcard include/config/libukswrand/chacha.h) \
    $(wildcard include/config/have/smp.h) \
    $(wildcard include/config/have/syscall.h) \
    $(wildcard include/config/have/x86pku.h) \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/string.h \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/nolibc-internal/shareddefs.h \
    $(wildcard include/config/have/time.h) \
  /home/terrylos/Thesis/unikraft/include/uk/config.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/types.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/intsizes.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/types.h \
  /home/terrylos/Thesis/unikraft/lib/uktime/include/uk/time_types.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/uk/plat/common/sections.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/cpu.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/cpu_defs.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/uk/plat/common/sw_ctx.h \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/stdint.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/limits.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/limits.h \
    $(wildcard include/config/stack/size/page/order.h) \
  /home/terrylos/Thesis/unikraft/include/uk/plat/thread.h \
  /home/terrylos/Thesis/unikraft/include/uk/essentials.h \
    $(wildcard include/config/libnewlibc.h) \
    $(wildcard include/config/have/sched.h) \
  /home/terrylos/Thesis/unikraft/lib/ukdebug/include/uk/assert.h \
    $(wildcard include/config/libukdebug/enable/assert.h) \
  /home/terrylos/Thesis/unikraft/include/uk/plat/bootstrap.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/lcpu.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/lcpu.h \
  /home/terrylos/Thesis/unikraft/lib/ukdebug/include/uk/print.h \
    $(wildcard include/config/libukdebug/printd.h) \
    $(wildcard include/config/libukdebug/printk/crit.h) \
    $(wildcard include/config/libukdebug/printk/err.h) \
    $(wildcard include/config/libukdebug/printk/warn.h) \
    $(wildcard include/config/libukdebug/printk/info.h) \
    $(wildcard include/config/libukdebug/printk.h) \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/stdarg.h \
  /home/terrylos/Thesis/unikraft/lib/ukalloc/include/uk/alloc.h \
    $(wildcard include/config/libukalloc/ifstats.h) \
    $(wildcard include/config/libukalloc/ifmalloc.h) \
    $(wildcard include/config/libukalloc/ifstats/perlib.h) \
    $(wildcard include/config/libukalloc/ifstats/global.h) \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/errno.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/traps.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/include/kvm/config.h \
    $(wildcard include/config/arch/arm/64.h) \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/inttypes.h \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/sys/types.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/include/kvm/console.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/include/kvm/intctrl.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/include/kvm-x86/multiboot.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/include/kvm-x86/multiboot_defs.h \
  /home/terrylos/Thesis/unikraft/include/uk/plat/console.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/acpi/acpi.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/acpi/sdt.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/acpi/madt.h \
  /home/terrylos/Thesis/unikraft/lib/ukswrand/include/uk/swrand.h \
  /home/terrylos/Thesis/unikraft/include/uk/plat/lcpu.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/time.h \
  /home/terrylos/Thesis/unikraft/include/uk/plat/time.h \
    $(wildcard include/config/hz.h) \

/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/setup.o: $(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/setup.o)

$(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/setup.o):
