cmd_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/trace.common.o := ""gcc -nostdlib -U __linux__ -U __FreeBSD__ -U __sun__ -fno-stack-protector -Wall -Wextra -D __Unikraft__ -DUK_CODENAME="Mimas" -DUK_VERSION=0.7 -DUK_FULLVERSION=0.7.0~3e14fc5-custom -fno-tree-sra -fno-split-stack -nostdinc -Os -fno-omit-frame-pointer -flto -fno-PIC -fhosted -ffreestanding -fno-tree-loop-distribute-patterns   -I/home/terrylos/Thesis/apps/app-helloworld/build/include -I/home/terrylos/Thesis/unikraft/arch/x86/x86_64/include -I/home/terrylos/Thesis/unikraft/include -I/home/terrylos/Thesis/unikraft/lib/devfs/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/arch/x86_64 -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/arch/generic -I/home/terrylos/Thesis/unikraft/lib/posix-user/include -I/home/terrylos/Thesis/unikraft/lib/posix-user/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/syscall_shim/include -I/home/terrylos/Thesis/unikraft/lib/ukalloc/include -I/home/terrylos/Thesis/unikraft/lib/ukallocbbuddy/include -I/home/terrylos/Thesis/unikraft/lib/ukargparse/include -I/home/terrylos/Thesis/unikraft/lib/ukboot/include -I/home/terrylos/Thesis/unikraft/lib/ukbus/include -I/home/terrylos/Thesis/unikraft/lib/ukdebug/include -I/home/terrylos/Thesis/unikraft/lib/uklibparam/include -I/home/terrylos/Thesis/unikraft/lib/uksglist/include -I/home/terrylos/Thesis/unikraft/lib/uksp/include -I/home/terrylos/Thesis/unikraft/lib/ukswrand/include -I/home/terrylos/Thesis/unikraft/lib/uktime/include -I/home/terrylos/Thesis/unikraft/lib/uktime/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/uktimeconv/include -I/home/terrylos/Thesis/unikraft/lib/vfscore/include  -I/home/terrylos/Thesis/unikraft/plat/kvm/include -I/home/terrylos/Thesis/unikraft/plat/common/include -I/home/terrylos/Thesis/unikraft/plat/drivers/include   -D__X86_64__ -m64 -mno-red-zone -fno-asynchronous-unwind-tables -fno-reorder-blocks -mtune=generic -DCC_VERSION=12.0 -fno-builtin-printf -fno-builtin-fprintf -fno-builtin-sprintf -fno-builtin-snprintf -fno-builtin-vprintf -fno-builtin-vfprintf -fno-builtin-vsprintf -fno-builtin-vsnprintf -fno-builtin-scanf -fno-builtin-fscanf -fno-builtin-sscanf -fno-builtin-vscanf -fno-builtin-vfscanf -fno-builtin-vsscanf -DCONFIG_UK_NETDEV_SCRATCH_SIZE=0  -DKVMPLAT     -g3 -D__LIBNAME__=libkvmplat -D__BASENAME__=trace.c -D__VARIANT__=common -c /home/terrylos/Thesis/unikraft/plat/common/x86/trace.c -o /home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/trace.common.o -Wp,-MD,/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/.trace.common.o.d

source_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/trace.common.o := /home/terrylos/Thesis/unikraft/plat/common/x86/trace.c

deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/trace.common.o := \
  /home/terrylos/Thesis/unikraft/plat/common/include/uk/plat/common/trace.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/lcpu.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/types.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/intsizes.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/types.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/lcpu.h \
  /home/terrylos/Thesis/unikraft/lib/ukdebug/include/uk/print.h \
    $(wildcard include/config/libukdebug/printd.h) \
    $(wildcard include/config/libukdebug/printk/crit.h) \
    $(wildcard include/config/libukdebug/printk/err.h) \
    $(wildcard include/config/libukdebug/printk/warn.h) \
    $(wildcard include/config/libukdebug/printk/info.h) \
    $(wildcard include/config/libukdebug/printk.h) \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/stdarg.h \
  /home/terrylos/Thesis/unikraft/include/uk/essentials.h \
    $(wildcard include/config/libnewlibc.h) \
    $(wildcard include/config/have/sched.h) \
  /home/terrylos/Thesis/unikraft/include/uk/config.h \

/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/trace.common.o: $(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/trace.common.o)

$(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmplat/trace.common.o):
