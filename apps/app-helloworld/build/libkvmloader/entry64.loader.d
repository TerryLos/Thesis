cmd_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/entry64.loader.o := ""gcc -nostdlib -U __linux__ -U __FreeBSD__ -U __sun__ -fno-stack-protector -Wall -Wextra -D __Unikraft__ -DUK_CODENAME="Mimas" -DUK_VERSION=0.7 -DUK_FULLVERSION=0.7.0~5e4e48b-custom -fno-tree-sra -fno-split-stack -nostdinc -O2 -fno-omit-frame-pointer -no-pie   -I/home/terrylos/Thesis/apps/app-helloworld/build/include -I/home/terrylos/Thesis/unikraft/arch/x86/x86_64/include -I/home/terrylos/Thesis/unikraft/include -I/home/terrylos/Thesis/unikraft/lib/uklibparam/include  -I/home/terrylos/Thesis/unikraft/plat/kvm/include -I/home/terrylos/Thesis/unikraft/plat/common/include   -D__X86_64__ -m64 -mno-red-zone -fno-asynchronous-unwind-tables -fno-reorder-blocks -mtune=generic -DCC_VERSION=11.2 -D__ASSEMBLY__   -DKVMPLAT     -g3 -D__LIBNAME__=libkvmloader -D__BASENAME__=entry64.S -D__VARIANT__=loader -c /home/terrylos/Thesis/unikraft/plat/kvm/loader/entry64.S -o /home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/entry64.loader.o -Wp,-MD,/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/.entry64.loader.o.d

source_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/entry64.loader.o := /home/terrylos/Thesis/unikraft/plat/kvm/loader/entry64.S

deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/entry64.loader.o := \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/cpu_defs.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/include/kvm-x86/traps.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/traps.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/lcpu.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/lcpu.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/include/kvm-x86/multiboot_defs.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/loader/pagetable.S \

/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/entry64.loader.o: $(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/entry64.loader.o)

$(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/entry64.loader.o):
