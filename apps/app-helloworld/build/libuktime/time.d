cmd_/home/terrylos/thesis/apps/app-helloworld/build/libuktime/time.o := ""gcc -nostdlib -U __linux__ -U __FreeBSD__ -U __sun__ -fno-stack-protector -Wall -Wextra -D __Unikraft__ -DUK_CODENAME="Mimas" -DUK_VERSION=0.7 -DUK_FULLVERSION=0.7.0~594b73c -fno-tree-sra -fno-split-stack -nostdinc -O2 -fno-omit-frame-pointer -fno-PIC -fhosted -ffreestanding -fno-tree-loop-distribute-patterns   -I/home/terrylos/thesis/apps/app-helloworld/build/include -I/home/terrylos/thesis/unikraft/arch/x86/x86_64/include -I/home/terrylos/thesis/unikraft/include -I/home/terrylos/thesis/unikraft/lib/devfs/include -I/home/terrylos/thesis/unikraft/lib/nolibc/include -I/home/terrylos/thesis/unikraft/lib/nolibc/arch/x86_64 -I/home/terrylos/thesis/unikraft/lib/nolibc/musl-imported/include -I/home/terrylos/thesis/unikraft/lib/nolibc/musl-imported/arch/generic -I/home/terrylos/thesis/unikraft/lib/posix-user/include -I/home/terrylos/thesis/unikraft/lib/posix-user/musl-imported/include -I/home/terrylos/thesis/unikraft/lib/syscall_shim/include -I/home/terrylos/thesis/unikraft/lib/ukalloc/include -I/home/terrylos/thesis/unikraft/lib/ukallocbbuddy/include -I/home/terrylos/thesis/unikraft/lib/ukargparse/include -I/home/terrylos/thesis/unikraft/lib/ukboot/include -I/home/terrylos/thesis/unikraft/lib/ukbus/include -I/home/terrylos/thesis/unikraft/lib/ukdebug/include -I/home/terrylos/thesis/unikraft/lib/uklibparam/include -I/home/terrylos/thesis/unikraft/lib/uksglist/include -I/home/terrylos/thesis/unikraft/lib/uksp/include -I/home/terrylos/thesis/unikraft/lib/uktime/include -I/home/terrylos/thesis/unikraft/lib/uktime/musl-imported/include -I/home/terrylos/thesis/unikraft/lib/uktimeconv/include -I/home/terrylos/thesis/unikraft/lib/vfscore/include     -D__X86_64__ -m64 -mno-red-zone -fno-asynchronous-unwind-tables -fno-reorder-blocks -mtune=generic -DCC_VERSION=11.2 -fno-builtin-printf -fno-builtin-fprintf -fno-builtin-sprintf -fno-builtin-snprintf -fno-builtin-vprintf -fno-builtin-vfprintf -fno-builtin-vsprintf -fno-builtin-vsnprintf -fno-builtin-scanf -fno-builtin-fscanf -fno-builtin-sscanf -fno-builtin-vscanf -fno-builtin-vfscanf -fno-builtin-vsscanf -DCONFIG_UK_NETDEV_SCRATCH_SIZE=0       -g3 -D__LIBNAME__=libuktime -D__BASENAME__=time.c -c /home/terrylos/thesis/unikraft/lib/uktime/time.c -o /home/terrylos/thesis/apps/app-helloworld/build/libuktime/time.o -Wp,-MD,/home/terrylos/thesis/apps/app-helloworld/build/libuktime/.time.o.d

source_/home/terrylos/thesis/apps/app-helloworld/build/libuktime/time.o := /home/terrylos/thesis/unikraft/lib/uktime/time.c

deps_/home/terrylos/thesis/apps/app-helloworld/build/libuktime/time.o := \
    $(wildcard include/config/have/sched.h) \
  /home/terrylos/thesis/unikraft/lib/nolibc/include/errno.h \
  /home/terrylos/thesis/unikraft/lib/uktime/musl-imported/include/time.h \
    $(wildcard include/config/libnolibc.h) \
  /home/terrylos/thesis/unikraft/include/uk/config.h \
  /home/terrylos/thesis/unikraft/lib/nolibc/include/sys/types.h \
  /home/terrylos/thesis/unikraft/include/uk/arch/types.h \
  /home/terrylos/thesis/unikraft/arch/x86/x86_64/include/uk/asm/intsizes.h \
  /home/terrylos/thesis/unikraft/arch/x86/x86_64/include/uk/asm/types.h \
  /home/terrylos/thesis/unikraft/lib/nolibc/include/nolibc-internal/shareddefs.h \
    $(wildcard include/config/have/time.h) \
  /home/terrylos/thesis/unikraft/lib/uktime/include/uk/time_types.h \
  /home/terrylos/thesis/unikraft/lib/nolibc/include/unistd.h \
    $(wildcard include/config/libposix/sysinfo.h) \
    $(wildcard include/config/libposix/process.h) \
    $(wildcard include/config/libvfscore.h) \
    $(wildcard include/config/libuksignal.h) \
  /home/terrylos/thesis/unikraft/lib/uktime/musl-imported/include/sys/time.h \
  /home/terrylos/thesis/unikraft/include/uk/plat/time.h \
    $(wildcard include/config/hz.h) \
  /home/terrylos/thesis/unikraft/include/uk/arch/time.h \
  /home/terrylos/thesis/unikraft/include/uk/arch/limits.h \
  /home/terrylos/thesis/unikraft/arch/x86/x86_64/include/uk/asm/limits.h \
    $(wildcard include/config/stack/size/page/order.h) \
  /home/terrylos/thesis/unikraft/lib/nolibc/include/stdint.h \
  /home/terrylos/thesis/unikraft/lib/ukdebug/include/uk/print.h \
    $(wildcard include/config/libukdebug/printd.h) \
    $(wildcard include/config/libukdebug/printk/crit.h) \
    $(wildcard include/config/libukdebug/printk/err.h) \
    $(wildcard include/config/libukdebug/printk/warn.h) \
    $(wildcard include/config/libukdebug/printk/info.h) \
    $(wildcard include/config/libukdebug/printk.h) \
  /home/terrylos/thesis/unikraft/lib/nolibc/include/stdarg.h \
  /home/terrylos/thesis/unikraft/include/uk/arch/lcpu.h \
  /home/terrylos/thesis/unikraft/arch/x86/x86_64/include/uk/asm/lcpu.h \
  /home/terrylos/thesis/unikraft/include/uk/essentials.h \
    $(wildcard include/config/libnewlibc.h) \
  /home/terrylos/thesis/unikraft/lib/syscall_shim/include/uk/syscall.h \
    $(wildcard include/config/libsyscall/shim.h) \
    $(wildcard include/config/libsyscall/shim/nowrapper.h) \
    $(wildcard include/config/libsyscall/shim/debug.h) \
  /home/terrylos/thesis/unikraft/include/uk/errptr.h \
  /home/terrylos/thesis/unikraft/include/uk/plat/lcpu.h \
    $(wildcard include/config/have/smp.h) \

/home/terrylos/thesis/apps/app-helloworld/build/libuktime/time.o: $(deps_/home/terrylos/thesis/apps/app-helloworld/build/libuktime/time.o)

$(deps_/home/terrylos/thesis/apps/app-helloworld/build/libuktime/time.o):
