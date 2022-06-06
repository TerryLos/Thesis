#!/bin/bash

gaulthier () {
	cd gaulthier
	rm data_ksm.json
	python3 ksm.py &
	xterm -e ./run.sh ftp_aslr_plt &
	xterm -e ./run.sh sqlite_aslr_plt &
	xterm -e ./run.sh nginx_aslr_plt &
	sleep 60 
	kill -2 $(ps -ef | grep "ksm.py"|awk '{print $2}')
	kill -9 $(pidof qemu-system-x86_64)
}

gaulthier


