cmd_/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/cpu_vectors_x86_64.o := ""gcc -nostdlib -U __linux__ -U __FreeBSD__ -U __sun__ -fno-stack-protector -Wall -Wextra -D __Unikraft__ -DUK_CODENAME="Mimas" -DUK_VERSION=0.7 -DUK_FULLVERSION=0.7.0~594b73c -fno-tree-sra -fno-split-stack -nostdinc -O2 -fno-omit-frame-pointer -fno-PIC -fhosted -ffreestanding -fno-tree-loop-distribute-patterns   -I/home/terrylos/thesis/apps/app-helloworld/build/include -I/home/terrylos/thesis/unikraft/arch/x86/x86_64/include -I/home/terrylos/thesis/unikraft/include -I/home/terrylos/thesis/unikraft/lib/uklibparam/include  -I/home/terrylos/thesis/unikraft/plat/kvm/include -I/home/terrylos/thesis/unikraft/plat/common/include   -D__X86_64__ -m64 -mno-red-zone -fno-asynchronous-unwind-tables -fno-reorder-blocks -mtune=generic -DCC_VERSION=11.2 -D__ASSEMBLY__   -DKVMPLAT     -g3 -D__LIBNAME__=libkvmplat -D__BASENAME__=cpu_vectors_x86_64.S -c /home/terrylos/thesis/unikraft/plat/kvm/x86/cpu_vectors_x86_64.S -o /home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/cpu_vectors_x86_64.o -Wp,-MD,/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/.cpu_vectors_x86_64.o.d

source_/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/cpu_vectors_x86_64.o := /home/terrylos/thesis/unikraft/plat/kvm/x86/cpu_vectors_x86_64.S

deps_/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/cpu_vectors_x86_64.o := \
  /home/terrylos/thesis/unikraft/plat/common/include/x86/traps.h \
  /home/terrylos/thesis/unikraft/include/uk/arch/lcpu.h \
  /home/terrylos/thesis/unikraft/arch/x86/x86_64/include/uk/asm/lcpu.h \

/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/cpu_vectors_x86_64.o: $(deps_/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/cpu_vectors_x86_64.o)

$(deps_/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/cpu_vectors_x86_64.o):
