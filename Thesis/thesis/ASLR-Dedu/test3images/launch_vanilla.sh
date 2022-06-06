#!/bin/bash

vanilla () {
	cd vanilla
	rm data_ksm.json
	python3 ksm.py &
	xterm -e ./ftp.sh &
	xterm -e ./sqlite.sh &
	xterm -e ./nginx.sh &
	sleep 60 
	kill -2 $(ps -ef | grep "ksm.py"|awk '{print $2}')
	kill -9 $(pidof qemu-system-x86_64)
}

vanilla


