cmd_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/entry64.o := ""gcc -nostdlib -U __linux__ -U __FreeBSD__ -U __sun__ -fno-stack-protector -Wall -Wextra -D __Unikraft__ -DUK_CODENAME="Mimas" -DUK_VERSION=0.7 -DUK_FULLVERSION=0.7.0~b224133-custom -fno-tree-sra -fno-split-stack -nostdinc -Os -fno-omit-frame-pointer -fdata-sections -ffunction-sections -flto -fno-PIC -fhosted -ffreestanding -fno-tree-loop-distribute-patterns   -I/home/terrylos/Thesis/apps/app-helloworld/build/include -I/home/terrylos/Thesis/unikraft/arch/x86/x86_64/include -I/home/terrylos/Thesis/unikraft/include -I/home/terrylos/Thesis/unikraft/lib/uklibparam/include  -I/home/terrylos/Thesis/unikraft/plat/kvm/include -I/home/terrylos/Thesis/unikraft/plat/common/include   -D__X86_64__ -m64 -mno-red-zone -fno-asynchronous-unwind-tables -fno-reorder-blocks -mtune=generic -DCC_VERSION=12.0 -D__ASSEMBLY__   -DKVMPLAT     -g0 -D__LIBNAME__=libkvmplat -D__BASENAME__=entry64.S -c /home/terrylos/Thesis/unikraft/plat/kvm/x86/entry64.S -o /home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/entry64.o -Wp,-MD,/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/.entry64.o.d

source_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/entry64.o := /home/terrylos/Thesis/unikraft/plat/kvm/x86/entry64.S

deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/entry64.o := \
    $(wildcard include/config/have/x86pku.h) \
    $(wildcard include/config/memory/dedup/aslr.h) \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/cpu_defs.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/include/kvm-x86/traps.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/traps.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/lcpu.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/lcpu.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/include/kvm-x86/multiboot_defs.h \
  /home/terrylos/Thesis/unikraft/include/uk/config.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/x86/pagetable.S \

/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/entry64.o: $(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/entry64.o)

$(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/entry64.o):
