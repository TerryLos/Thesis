cmd_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmvirtio/virtio_bus.o := ""gcc -nostdlib -U __linux__ -U __FreeBSD__ -U __sun__ -fno-stack-protector -Wall -Wextra -D __Unikraft__ -DUK_CODENAME="Mimas" -DUK_VERSION=0.7 -DUK_FULLVERSION=0.7.0~0cacb10-custom -fno-tree-sra -fno-split-stack -nostdinc -O2 -fno-omit-frame-pointer -fno-PIC -fhosted -ffreestanding -fno-tree-loop-distribute-patterns   -I/home/terrylos/Thesis/apps/app-helloworld/build/include -I/home/terrylos/Thesis/unikraft/arch/x86/x86_64/include -I/home/terrylos/Thesis/unikraft/include -I/home/terrylos/Thesis/unikraft/lib/devfs/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/arch/x86_64 -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/nolibc/musl-imported/arch/generic -I/home/terrylos/Thesis/unikraft/lib/posix-user/include -I/home/terrylos/Thesis/unikraft/lib/posix-user/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/syscall_shim/include -I/home/terrylos/Thesis/unikraft/lib/ukalloc/include -I/home/terrylos/Thesis/unikraft/lib/ukallocbbuddy/include -I/home/terrylos/Thesis/unikraft/lib/ukargparse/include -I/home/terrylos/Thesis/unikraft/lib/ukboot/include -I/home/terrylos/Thesis/unikraft/lib/ukbus/include -I/home/terrylos/Thesis/unikraft/lib/ukdebug/include -I/home/terrylos/Thesis/unikraft/lib/uklibparam/include -I/home/terrylos/Thesis/unikraft/lib/uksglist/include -I/home/terrylos/Thesis/unikraft/lib/uksp/include -I/home/terrylos/Thesis/unikraft/lib/ukswrand/include -I/home/terrylos/Thesis/unikraft/lib/uktime/include -I/home/terrylos/Thesis/unikraft/lib/uktime/musl-imported/include -I/home/terrylos/Thesis/unikraft/lib/uktimeconv/include -I/home/terrylos/Thesis/unikraft/lib/vfscore/include  -I/home/terrylos/Thesis/unikraft/plat/kvm/include -I/home/terrylos/Thesis/unikraft/plat/common/include -I/home/terrylos/Thesis/unikraft/plat/drivers/include   -D__X86_64__ -m64 -mno-red-zone -fno-asynchronous-unwind-tables -fno-reorder-blocks -mtune=generic -DCC_VERSION=12.0 -fno-builtin-printf -fno-builtin-fprintf -fno-builtin-sprintf -fno-builtin-snprintf -fno-builtin-vprintf -fno-builtin-vfprintf -fno-builtin-vsprintf -fno-builtin-vsnprintf -fno-builtin-scanf -fno-builtin-fscanf -fno-builtin-sscanf -fno-builtin-vscanf -fno-builtin-vfscanf -fno-builtin-vsscanf -DCONFIG_UK_NETDEV_SCRATCH_SIZE=0       -g3 -D__LIBNAME__=libkvmvirtio -D__BASENAME__=virtio_bus.c -c /home/terrylos/Thesis/unikraft/plat/drivers/virtio/virtio_bus.c -o /home/terrylos/Thesis/apps/app-helloworld/build/libkvmvirtio/virtio_bus.o -Wp,-MD,/home/terrylos/Thesis/apps/app-helloworld/build/libkvmvirtio/.virtio_bus.o.d

source_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmvirtio/virtio_bus.o := /home/terrylos/Thesis/unikraft/plat/drivers/virtio/virtio_bus.c

deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmvirtio/virtio_bus.o := \
  /home/terrylos/Thesis/unikraft/include/uk/config.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/types.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/intsizes.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/types.h \
  /home/terrylos/Thesis/unikraft/include/uk/list.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/atomic.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/lcpu.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/lcpu.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/atomic.h \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/stddef.h \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/nolibc-internal/shareddefs.h \
    $(wildcard include/config/have/time.h) \
  /home/terrylos/Thesis/unikraft/lib/uktime/include/uk/time_types.h \
  /home/terrylos/Thesis/unikraft/include/uk/compat_list.h \
  /home/terrylos/Thesis/unikraft/lib/ukalloc/include/uk/alloc.h \
    $(wildcard include/config/libukalloc/ifstats.h) \
    $(wildcard include/config/libukalloc/ifmalloc.h) \
    $(wildcard include/config/libukalloc/ifstats/perlib.h) \
    $(wildcard include/config/libukalloc/ifstats/global.h) \
  /home/terrylos/Thesis/unikraft/lib/ukdebug/include/uk/assert.h \
    $(wildcard include/config/libukdebug/enable/assert.h) \
  /home/terrylos/Thesis/unikraft/include/uk/plat/bootstrap.h \
  /home/terrylos/Thesis/unikraft/include/uk/essentials.h \
    $(wildcard include/config/libnewlibc.h) \
    $(wildcard include/config/have/sched.h) \
  /home/terrylos/Thesis/unikraft/lib/ukdebug/include/uk/print.h \
    $(wildcard include/config/libukdebug/printd.h) \
    $(wildcard include/config/libukdebug/printk/crit.h) \
    $(wildcard include/config/libukdebug/printk/err.h) \
    $(wildcard include/config/libukdebug/printk/warn.h) \
    $(wildcard include/config/libukdebug/printk/info.h) \
    $(wildcard include/config/libukdebug/printk.h) \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/stdarg.h \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/errno.h \
  /home/terrylos/Thesis/unikraft/lib/ukbus/include/uk/bus.h \
  /home/terrylos/Thesis/unikraft/include/uk/ctors.h \
  /home/terrylos/Thesis/unikraft/include/uk/prio.h \
  /home/terrylos/Thesis/unikraft/plat/drivers/include/virtio/virtio_ids.h \
  /home/terrylos/Thesis/unikraft/plat/drivers/include/virtio/virtio_config.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/uk/plat/common/cpu.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/cpu.h \
    $(wildcard include/config/have/syscall.h) \
    $(wildcard include/config/have/x86pku.h) \
  /home/terrylos/Thesis/unikraft/plat/common/include/x86/cpu_defs.h \
  /home/terrylos/Thesis/unikraft/plat/common/include/uk/plat/common/sw_ctx.h \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/stdint.h \
  /home/terrylos/Thesis/unikraft/include/uk/arch/limits.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/limits.h \
    $(wildcard include/config/stack/size/page/order.h) \
  /home/terrylos/Thesis/unikraft/include/uk/plat/thread.h \
  /home/terrylos/Thesis/unikraft/lib/nolibc/include/string.h \
  /home/terrylos/Thesis/unikraft/plat/drivers/include/virtio/virtio_bus.h \
  /home/terrylos/Thesis/unikraft/include/uk/errptr.h \
  /home/terrylos/Thesis/unikraft/plat/drivers/include/virtio/virtqueue.h \
  /home/terrylos/Thesis/unikraft/lib/uksglist/include/uk/sglist.h \
    $(wildcard include/config/libukalloc.h) \
    $(wildcard include/config/libuknetdev.h) \
    $(wildcard include/config/libuknet.h) \
  /home/terrylos/Thesis/unikraft/include/uk/refcount.h \
    $(wildcard include/config/libukdebug.h) \
  /home/terrylos/Thesis/unikraft/plat/drivers/include/virtio/virtio_ring.h \
  /home/terrylos/Thesis/unikraft/plat/drivers/include/virtio/virtio_types.h \

/home/terrylos/Thesis/apps/app-helloworld/build/libkvmvirtio/virtio_bus.o: $(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmvirtio/virtio_bus.o)

$(deps_/home/terrylos/Thesis/apps/app-helloworld/build/libkvmvirtio/virtio_bus.o):
