#!/bin/sh

echo 1 | sudo tee /sys/kernel/mm/ksm/run
echo 1 | sudo tee /sys/kernel/mm/ksm/use_zero_pages


for i in {1..10}
do
qemu-system-x86_64 -kernel app-ftp_kvm-x86_64.dbg-$i -fsdev local,id=myid,path=$(pwd)/rootfs/,security_model=none \
	-device virtio-9p-pci,fsdev=myid,mount_tag=fs0 -enable-kvm -m 20M &
done

sleep 0.1s
for i in {1..100}
do
python3 compute_frames.py --process qemu-system-x86_64 --smap --csv "./../csv/vanilla.csv"
sleep 0.5s
done
echo "Done"
