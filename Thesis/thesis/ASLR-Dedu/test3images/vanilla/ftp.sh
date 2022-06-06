#!/bin/bash
qemu-system-x86_64 -m 20M -enable-kvm -nographic  -device isa-debug-exit -fsdev local,id=myid,path=test,security_model=none -device virtio-9p-pci,fsdev=myid,mount_tag=test,disable-modern=on,disable-legacy=off  -cpu host -kernel app-ftp_kvm-x86_64
