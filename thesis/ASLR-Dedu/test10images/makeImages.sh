#!/bin/bash
FILE=vanilla
WORKDIR=$(pwd)
cd ./../../../apps/app-ftp/
for i in {1..10}
do
	make -j12
	if [ $? -eq 0 ]
	then
	cp ./build/app-ftp_kvm-x86_64.dbg $WORKDIR/$FILE/app-ftp_kvm-x86_64.dbg-$i
	else
	i=($i-1)
	fi
done
