cmd_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/libelf_msize.loader.o := ""gcc -nostdlib -U __linux__ -U __FreeBSD__ -U __sun__ -fno-stack-protector -Wall -Wextra -D __Unikraft__ -DUK_CODENAME="Mimas" -DUK_VERSION=0.7 -DUK_FULLVERSION=0.7.0~5e4e48b-custom -fno-tree-sra -fno-split-stack -nostdinc -O2 -fno-omit-frame-pointer -no-pie     -I/home/terrylos/Thesis/apps/app-helloworld/build/include -I/home/terrylos/Thesis/unikraft/arch/x86/x86_64/include -I/home/terrylos/Thesis/unikraft/include -I/home/terrylos/Thesis/unikraft/lib/devfs/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/arch/x86_64 -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/arch/generic -I/home/terrylos/Thesis/unikraft/lib/posix-user/include -I/home/terrylos/Thesis/unikraft/lib/posix-user/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/syscall_shim/include -I/home/terrylos/Thesis/unikraft/lib/ukalloc/include -I/home/terrylos/Thesis/unikraft/lib/ukallocbbuddy/include -I/home/terrylos/Thesis/unikraft/lib/ukargparse/include -I/home/terrylos/Thesis/unikraft/lib/ukboot/include -I/home/terrylos/Thesis/unikraft/lib/ukbus/include -I/home/terrylos/Thesis/unikraft/lib/ukdebug/include -I/home/terrylos/Thesis/unikraft/lib/uklibparam/include -I/home/terrylos/Thesis/unikraft/lib/uksglist/include -I/home/terrylos/Thesis/unikraft/lib/uksp/include -I/home/terrylos/Thesis/unikraft/lib/ukswrand/include -I/home/terrylos/Thesis/unikraft/lib/uktime/include -I/home/terrylos/Thesis/unikraft/lib/uktime/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/uktimeconv/include -I/home/terrylos/Thesis/unikraft/lib/vfscore/include  -I/home/terrylos/Thesis/unikraft/plat/kvm/include -I/home/terrylos/Thesis/unikraft/plat/common/include -I/home/terrylos/Thesis/unikraft/plat/drivers/include -I/home/terrylos/Thesis/unikraft/plat/kvm/loader/include -I/home/terrylos/Thesis/unikraft/arch/x86/x86_64/include -I/home/terrylos/Thesis/unikraft/include  -I/home/terrylos/Thesis/unikraft/lib/ukboot/include -I/home/terrylos/Thesis/unikraft/lib/ukswrand/include -I/home/terrylos/Thesis/unikraft/lib/posix-user/include -I/home/terrylos/Thesis/unikraft/lib/posix-user/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/posix-sysinfo/include -I/home/daniel/Faculty/BachelorThesis/unikraft/lib/ukdebug/include -I/home/daniel/Faculty/BachelorThesis/unikraft/lib/ukargparse/include -I/home/terrylos/Thesis/unikraft/lib/uktimeconv/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/arch/x86_64 -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/arch/generic -I/home/terrylos/Thesis/unikraft/lib/ukalloc/include -I/home/terrylos/Thesis/unikraft/lib/ukallocbbuddy/include -I/home/terrylos/Thesis/unikraft/lib/uksched/include -I/home/terrylos/Thesis/unikraft/lib/ukschedcoop/include -I/home/terrylos/Thesis/unikraft/lib/syscall_shim/include -I/home/terrylos/Thesis/unikraft/lib/vfscore/include -I/home/terrylos/Thesis/unikraft/lib/devfs/include -I/home/terrylos/Thesis/unikraft/lib/uklock/include -I/home/terrylos/Thesis/unikraft/lib/ukmpi/include -I/home/terrylos/Thesis/unikraft/lib/ukbus/include -I/home/terrylos/Thesis/unikraft/lib/uksglist/include -I/home/terrylos/Thesis/unikraft/lib/uknetdev/include -I/home/terrylos/Thesis/unikraft/lib/uklibparam/include -I/home/terrylos/Thesis/unikraft/lib/uktime/include -I/home/terrylos/Thesis/unikraft/lib/uktime/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/posix-process/include -I/home/terrylos/Thesis/unikraft/lib/posix-process/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/posix-process/musl-imported/arch/generic -I/home/terrylos/Thesis/unikraft/lib/uksp/include -I/home/terrylos/Thesis/unikraft/lib/ukallocbbuddy/include -I/home/terrylos/Thesis/unikraft/lib/ukalloc/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/arch/x86_64 -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/arch/generic -I/home/terrylos/Thesis/unikraft/lib/ukswrand/include -I/home/terrylos/Thesis/unikraft/plat/kvm/loader/elfloader -I/home/terrylos/Thesis/unikraft/plat/kvm/loader/libelf -I/home/terrylos/Thesis/unikraft/plat/kvm/loader/libelf/include   -D__X86_64__ -m64 -mno-red-zone -fno-asynchronous-unwind-tables -fno-reorder-blocks -mtune=generic -DCC_VERSION=11.2 -fno-builtin-printf -fno-builtin-fprintf -fno-builtin-sprintf -fno-builtin-snprintf -fno-builtin-vprintf -fno-builtin-vfprintf -fno-builtin-vsprintf -fno-builtin-vsnprintf -fno-builtin-scanf -fno-builtin-fscanf -fno-builtin-sscanf -fno-builtin-vscanf -fno-builtin-vfscanf -fno-builtin-vsscanf -DCONFIG_UK_NETDEV_SCRATCH_SIZE=0  -DKVMPLAT     -g3 -D__LIBNAME__=libkvmloader -D__BASENAME__=libelf_msize.c -D__VARIANT__=loader -c /home/terrylos/Thesis/unikraft/plat/kvm/loader/libelf/libelf_msize.c -o /home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/libelf_msize.loader.o -Wp,-MD,/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/.libelf_msize.loader.o.d

source_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/libelf_msize.loader.o := /home/terrylos/Thesis/unikraft/plat/kvm/loader/libelf/libelf_msize.c

deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/libelf_msize.loader.o := \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/assert.h \
    $(wildcard include/config/libnolibc/ukdebug/assert.h) \
  /home/terrylos/Thesis/unikraft/include/uk/config.h \
  /home/terrylos/Thesis/unikraft/lib/ukdebug/include/uk/assert.h \
    $(wildcard include/config/libukdebug/enable/assert.h) \
  /home/terrylos/Thesis/unikraft/include/uk/plat/bootstrap.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/types.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/intsizes.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/types.h \
  /home/terrylos/Thesis/unikraft/include/uk/essentials.h \
    $(wildcard include/config/libnewlibc.h) \
    $(wildcard include/config/have/sched.h) \
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
  /home/terrylos/Thesis/unikraft/plat/kvm/loader/libelf/include/libelf.h \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/sys/types.h \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/nolibc-internal/shareddefs.h \
    $(wildcard include/config/have/time.h) \
  /home/terrylos/Thesis/unikraft/lib/uktime/include/uk/time_types.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/loader/libelf/include/elfdefinitions.h \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/stdint.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/limits.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/limits.h \
    $(wildcard include/config/stack/size/page/order.h) \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/string.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/loader/libelf/_libelf.h \
  /home/terrylos/Thesis/unikraft/plat/kvm/loader/libelf/_libelf_config.h \
    $(wildcard include/config/arch/x86/32.h) \
    $(wildcard include/config/arch/x86/64.h) \
    $(wildcard include/config/arch/arm/32.h) \
    $(wildcard include/config/arch/arm/64.h) \
  /home/terrylos/Thesis/unikraft/plat/kvm/loader/libelf/_elftc.h \

/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/libelf_msize.loader.o: $(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/libelf_msize.loader.o)

$(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmloader/libelf_msize.loader.o):
