cmd_/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/console.o := ""gcc -nostdlib -U __linux__ -U __FreeBSD__ -U __sun__ -fno-stack-protector -Wall -Wextra -D __Unikraft__ -DUK_CODENAME="Mimas" -DUK_VERSION=0.7 -DUK_FULLVERSION=0.7.0~594b73c -fno-tree-sra -fno-split-stack -nostdinc -O2 -fno-omit-frame-pointer -fno-PIC -fhosted -ffreestanding -fno-tree-loop-distribute-patterns   -I/home/terrylos/thesis/apps/app-helloworld/build/include -I/home/terrylos/thesis/unikraft/arch/x86/x86_64/include -I/home/terrylos/thesis/unikraft/include -I/home/terrylos/thesis/unikraft/lib/devfs/include -I/home/terrylos/thesis/unikraft/lib/nolibc/include -I/home/terrylos/thesis/unikraft/lib/nolibc/arch/x86_64 -I/home/terrylos/thesis/unikraft/lib/nolibc/musl-imported/include -I/home/terrylos/thesis/unikraft/lib/nolibc/musl-imported/arch/generic -I/home/terrylos/thesis/unikraft/lib/posix-user/include -I/home/terrylos/thesis/unikraft/lib/posix-user/musl-imported/include -I/home/terrylos/thesis/unikraft/lib/syscall_shim/include -I/home/terrylos/thesis/unikraft/lib/ukalloc/include -I/home/terrylos/thesis/unikraft/lib/ukallocbbuddy/include -I/home/terrylos/thesis/unikraft/lib/ukargparse/include -I/home/terrylos/thesis/unikraft/lib/ukboot/include -I/home/terrylos/thesis/unikraft/lib/ukbus/include -I/home/terrylos/thesis/unikraft/lib/ukdebug/include -I/home/terrylos/thesis/unikraft/lib/uklibparam/include -I/home/terrylos/thesis/unikraft/lib/uksglist/include -I/home/terrylos/thesis/unikraft/lib/uksp/include -I/home/terrylos/thesis/unikraft/lib/uktime/include -I/home/terrylos/thesis/unikraft/lib/uktime/musl-imported/include -I/home/terrylos/thesis/unikraft/lib/uktimeconv/include -I/home/terrylos/thesis/unikraft/lib/vfscore/include  -I/home/terrylos/thesis/unikraft/plat/kvm/include -I/home/terrylos/thesis/unikraft/plat/common/include -I/home/terrylos/thesis/unikraft/plat/drivers/include   -D__X86_64__ -m64 -mno-red-zone -fno-asynchronous-unwind-tables -fno-reorder-blocks -mtune=generic -DCC_VERSION=11.2 -fno-builtin-printf -fno-builtin-fprintf -fno-builtin-sprintf -fno-builtin-snprintf -fno-builtin-vprintf -fno-builtin-vfprintf -fno-builtin-vsprintf -fno-builtin-vsnprintf -fno-builtin-scanf -fno-builtin-fscanf -fno-builtin-sscanf -fno-builtin-vscanf -fno-builtin-vfscanf -fno-builtin-vsscanf -DCONFIG_UK_NETDEV_SCRATCH_SIZE=0  -DKVMPLAT     -g3 -D__LIBNAME__=libkvmplat -D__BASENAME__=console.c -c /home/terrylos/thesis/unikraft/plat/kvm/x86/console.c -o /home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/console.o -Wp,-MD,/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/.console.o.d

source_/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/console.o := /home/terrylos/thesis/unikraft/plat/kvm/x86/console.c

deps_/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/console.o := \
    $(wildcard include/config/kvm/debug/vga/console.h) \
    $(wildcard include/config/kvm/kernel/vga/console.h) \
    $(wildcard include/config/kvm/debug/serial/console.h) \
    $(wildcard include/config/kvm/kernel/serial/console.h) \
  /home/terrylos/thesis/unikraft/include/uk/plat/console.h \
  /home/terrylos/thesis/unikraft/include/uk/essentials.h \
    $(wildcard include/config/libnewlibc.h) \
    $(wildcard include/config/have/sched.h) \
  /home/terrylos/thesis/unikraft/include/uk/config.h \
  /home/terrylos/thesis/unikraft/include/uk/arch/types.h \
  /home/terrylos/thesis/unikraft/arch/x86/x86_64/include/uk/asm/intsizes.h \
  /home/terrylos/thesis/unikraft/arch/x86/x86_64/include/uk/asm/types.h \
  /home/terrylos/thesis/unikraft/plat/kvm/include/kvm-x86/vga_console.h \
  /home/terrylos/thesis/unikraft/plat/kvm/include/kvm-x86/serial_console.h \

/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/console.o: $(deps_/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/console.o)

$(deps_/home/terrylos/thesis/apps/app-helloworld/build/libkvmplat/console.o):
