#!/usr/bin/sh

echo "Starting to run $1 Unikraft Images"
echo "Don't touch your keyboard during the process."
if [ $2 -eq 0 ]; then
	for i in $(seq 1 1 $1)
	do
		echo $i/$1
		qemu-system-x86_64 -m 1G -serial stdio -kernel ./build/entropy_kvm-x86_64 >> data.txt
		tmp=$(./relink_ELF.sh ~/Thesis/apps/entropy/build entropy_kvm-x86_64 ~/Thesis/unikraft 2>&1 >/dev/null)
	done
	echo "Done"
else
	for i in $(seq 1 1 $1)
	do
		echo $i/$1
		qemu-system-x86_64 -m 1G -serial stdio -kernel ./build/entropy_kvm-x86_64 >> data.txt
		tmp=$(make clean 2>&1 >/dev/null)
		tmp=$(make -j12 2>&1 >/dev/null)
	done
	echo "Done"
fi

