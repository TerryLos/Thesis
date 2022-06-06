#!/usr/bin/python3
import os
import sys
import time
import json
import signal
import subprocess
import threading

TIME = 0.1 #sec -- Use 0.1 for ms
KSM_PATH = '/sys/kernel/mm/ksm/' #/sys/kernel/mm/ksm/

ksm_data = {}
#num_vms = 0

thread_vm = None
kill_event = None

FILENAME="/home/wait.txt"

allowed_files = ['pages_sharing', 'pages_shared', 'ksm_zeroes_merged_pages', 'ksm_read_only_merged_pages', 'pages_unshared', 'pages_volatile']

def signal_handler(sig, frame):

    #kill_event.set()

    with open('data_ksm.json', 'w') as fp:
        json.dump(ksm_data, fp, sort_keys=True)#, indent=4)
    #thread_vm.join()
    runScript("echo '' > " + FILENAME)
    sys.exit(0)

'''
def get_number_VM(stop_event):

    global num_vms

    while not stop_event.wait(1):
        time.sleep(1)
        cmd = "ps -ef|grep 'qemu-system-x86_64'|wc|awk '{print $1}'"

        ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        output = ps.communicate()[0]
        num_vms = int(output)-1
'''

def get_ksm_info(path, timeScan):

    files = os.listdir(path)
    value_sharing = 0
    value_shared = 0
    ksm_data["diff"] = list()
    ksm_data["ratio"] = list()
    while True:
        time.sleep(timeScan)
        for file in files:
            if file in allowed_files:
                f = open(os.path.join(path, file), 'r')
                value_line = f.readline()
                f.close()
                if file not in ksm_data:
                    ksm_data[file] = list()
                
                if "sharing" in file:
                    value_sharing = int(value_line.strip())
                elif "shared" in file:
                    value_shared = int(value_line.strip())
                #elif "ksm_zeroes_merged_pages" in file:
                #    value_ksm_zeroes_merged_pages = int(value_line.strip())

                ksm_data[file].append((int(value_line.strip()), time.time()))
                ksm_data["diff"].append((value_sharing-value_shared, time.time()))
                if value_shared == 0:
                    value_shared = 1
                ksm_data["ratio"].append((value_sharing/value_shared, time.time()))

def runScript(cmd):
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ps.communicate()[0]

def main():
    runScript("echo 'RUN' > " + FILENAME)
    get_ksm_info(KSM_PATH, TIME)

if __name__== "__main__":

    print("Use CTRL+C to stop and save data to data_ksm.json")

    signal.signal(signal.SIGINT, signal_handler)

    #kill_event = threading.Event()
    #thread_vm = threading.Thread(target=get_number_VM, args=(kill_event,))
    #thread_vm.start()

    main()
