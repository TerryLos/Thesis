#!/bin/bash

cd vanilla
rm data_ksm.json
python3 ksm.py &

for i in {1..10}
do
qemu-system-x86_64 -kernel app-ftp_kvm-x86_64.dbg-$i -fsdev local,id=myid,path=$(pwd)/rootfs/,security_model=none \
	-device virtio-9p-pci,fsdev=myid,mount_tag=fs0 -enable-kvm -m 20M &
done
sleep 60 
kill -2 $(ps -ef | grep "ksm.py"|awk '{print $2}')
kill -9 $(pidof qemu-system-x86_64)

