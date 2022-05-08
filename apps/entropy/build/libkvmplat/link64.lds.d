cmd_/home/terrylos/Thesis/apps/entropy/build/libkvmplat/link64.lds := ""gcc -E -P -x assembler-with-cpp -nostdlib -U __linux__ -U __FreeBSD__ -U __sun__ -fno-stack-protector -Wall -Wextra -D __Unikraft__ -DUK_CODENAME="Mimas" -DUK_VERSION=0.7 -DUK_FULLVERSION=0.7.0~f267a5a-custom -fno-tree-sra -fno-split-stack -nostdinc -O2 -fno-omit-frame-pointer -fno-PIC -fhosted -ffreestanding -fno-tree-loop-distribute-patterns -I/home/terrylos/Thesis/apps/entropy/build/include -I/home/terrylos/Thesis/unikraft/arch/x86/x86_64/include -I/home/terrylos/Thesis/unikraft/include -I/home/terrylos/Thesis/unikraft/lib/uklibparam/include  -I/home/terrylos/Thesis/unikraft/plat/kvm/include -I/home/terrylos/Thesis/unikraft/plat/common/include   -D__X86_64__ -m64 -mno-red-zone -fno-asynchronous-unwind-tables -fno-reorder-blocks -mtune=generic -DCC_VERSION=12.0 -D__ASSEMBLY__   -DKVMPLAT    /home/terrylos/Thesis/unikraft/plat/kvm/x86/link64.lds.S -o /home/terrylos/Thesis/apps/entropy/build/libkvmplat/link64.lds -Wp,-MD,/home/terrylos/Thesis/apps/entropy/build/libkvmplat/.link64.lds.d

source_/home/terrylos/Thesis/apps/entropy/build/libkvmplat/link64.lds := /home/terrylos/Thesis/unikraft/plat/kvm/x86/link64.lds.S

deps_/home/terrylos/Thesis/apps/entropy/build/libkvmplat/link64.lds := \
  /home/terrylos/Thesis/unikraft/include/uk/arch/limits.h \
  /home/terrylos/Thesis/unikraft/include/uk/config.h \
  /home/terrylos/Thesis/unikraft/arch/x86/x86_64/include/uk/asm/limits.h \
    $(wildcard include/config/stack/size/page/order.h) \
  /home/terrylos/Thesis/unikraft/plat/common/include/uk/plat/common/common.lds.h \

/home/terrylos/Thesis/apps/entropy/build/libkvmplat/link64.lds: $(deps_/home/terrylos/Thesis/apps/entropy/build/libkvmplat/link64.lds)

$(deps_/home/terrylos/Thesis/apps/entropy/build/libkvmplat/link64.lds):
