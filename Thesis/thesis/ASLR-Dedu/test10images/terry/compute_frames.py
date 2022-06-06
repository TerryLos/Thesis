#!/usr/bin/python3

#
# Scan memory and to do some computations about memory of a specific process
#
# WARNING: Must be run as root for --pagemap
#
# usage: sudo compute_frames.py [-h] --process PROCESS
#
# Example:
#   sudo python compute_frames.py --process qemu-system-x86_64
# Others:
#
# cat /proc/$(pidof qemu-system-x86_64)/smaps
# cat /proc/$(pidof qemu-system-x86_64)/smaps_rollup
import re
import os
import sys
import time
import struct
import argparse
import subprocess

from collections import defaultdict
from datetime import datetime


OUT_CSV="test.csv"
PAGE_SIZE = os.sysconf("SC_PAGE_SIZE")
TO_MB = 1024 * 1024


header_csv = ""
######################################################################

class Process:
    def __init__(self, cmd):
        self.cmd = cmd
        self.pid = self.get_pid()
        self.memory = self.get_mem()
        self.list_info = list()
        self.maps_key = dict()

    def get_mem(self):
        mbqemu = ""
        for c in self.cmd[self.cmd.index("-m ")+1:]:
            if c.isdigit():
                mbqemu += c
            if c == "-":
                break
        
        return int(mbqemu)
    
    def get_pid(self):
        elems = self.cmd.split()
        if len(elems) == 0:
            sys.exit('Impossible to get pid of the process')
        return int(elems[1])

class AddrEntry:

    def get_pagecount(self, pfn):
      file_path = "/proc/kpagecount"
      offset = pfn * 8
      return read_entry(file_path, offset)

    def is_present(self, entry):
      return ((entry & (1 << 63)) != 0)

    def is_file_page(self, entry):
      return ((entry & (1 << 61)) != 0)

    def get_page_flags(self, pfn):
      file_path = "/proc/kpageflags"
      offset = pfn * 8
      return read_entry(file_path, offset)

    def __init__(self, pid, pfn, entry, vaddr):
        self.pid = pid
        self.pfn = pfn
        self.entry = entry
        self.virtual_address = vaddr
        self.physical_address = (pfn * PAGE_SIZE) + (vaddr % PAGE_SIZE)
        self.is_present = self.is_present(entry)
        self.is_file_page = self.is_file_page(entry)
        self.page_count = self.get_pagecount(pfn)
        self.page_flags = self.get_page_flags(pfn)

######################################################################


def read_entry(path, offset, size=8):
  with open(path, 'r') as f:
    f.seek(offset, 0)
    try:
        return struct.unpack('Q', f.read(size))[0]
    except Exception as ex:
        sys.stderr.write(str(ex))
        return -1

def get_pfn(entry):
      return entry & 0x7FFFFFFFFFFFFF

def get_pagemap_entry(pid, addr):
  
  maps_path = "/proc/{0}/pagemap".format(pid)
  if not os.path.isfile(maps_path):
    sys.exit("Process {0} doesn't exist.".format(pid))

  pagemap_entry_size = 8
  offset  = (addr / PAGE_SIZE) * pagemap_entry_size

  return read_entry(maps_path, offset)

def get_vaddr_info(pid, vaddr, maps_frames):
    entry = get_pagemap_entry(pid, vaddr)
    
    if entry != -1:
        pfn = get_pfn(entry)
        addrEntry = AddrEntry(pid, pfn, entry, vaddr)
        #if addrEntry.page_count > 1:
        #display_info(addrEntry)

        maps_frames[addrEntry.physical_address].append(addrEntry)

def display_info(entry):
    print("Virtual address: {}").format(hex(entry.virtual_address))
    print("Physical address: {}".format(hex(entry.physical_address)))
    print("PFN: {}").format(hex(entry.pfn))
    print("Is Present? : {}").format(entry.is_present)
    print("Is file-page: {}").format(entry.is_file_page)
    print("Page count: {}").format(entry.page_count)
    print("Page flags: {}").format(hex(entry.page_flags))
    print("---------------------------------------------")

######################################################################

def iterate_vma(process, lines, maps_frames, args):

    for l in lines:
        info = l.split()
        if len(info) <= 6:
            addresses = info[0].split("-")
            startAddr = int(addresses[0], 16)
            endAddr = int(addresses[1], 16)
            size = endAddr-startAddr
            
            if args.usevm:
                #Use a filter to limit the address space (only vma of the VM)
                if int(size/TO_MB) == process.memory and len(info) == 5:
                    # mapped to anonymous area
                    if args.pagemap:
                        for addr in range(startAddr, endAddr, PAGE_SIZE):
                            get_vaddr_info(process.pid, addr, maps_frames)
                    if args.smap:
                        process.list_info.append(info)
            else:
                if args.pagemap:
                    for addr in range(startAddr, endAddr, PAGE_SIZE):
                        get_vaddr_info(process.pid, addr, maps_frames)

def read_maps(process, maps_frames, args):
    maps_path = "/proc/{0}/maps".format(process.pid)
    if not os.path.isfile(maps_path):
        sys.exit("Process {0} doesn't exist.".format(process.pid))

    with open(maps_path,'r') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            iterate_vma(process, lines, maps_frames, args)

######################################################################

def process_smap(process, args):
    global header_csv

    if len(process.list_info) == 0:
        print("[ERROR] list_info of {} is empty".format(process.pid))
        sys.exit(1)
    
    if len(process.list_info) > 1:
        print("[WARNING] process {} as a size more than 1".format(process.pid))
        
    info = process.list_info[0]
    if len(info) != 5 and "-" not in info[0]:
        return None
    
    addrs = info[0].split("-")
    startAddr, endAddr = addrs[0], addrs[1]

    smaps_path = "/proc/{0}/smaps".format(process.pid)
    if not os.path.isfile(smaps_path):
        sys.exit("Process {0} doesn't exist.".format(process.pid))

    found=False
    init=False

    if len(header_csv) == 0:
        header_csv="timespan,vms,"
        init = True

    with open(smaps_path,'r') as file:
            lines = file.readlines()
            for l in lines:
                if endAddr+"-" in l:
                    found=False
                if found:
                    elems = l.split(":")
                    if len(elems) == 2:
                        key = elems[0].strip() + ","
                        value = elems[1].replace("\n", "").strip()
                        process.maps_key[key]= value.replace(" kB", "")
                        if init:
                            header_csv += key
                if startAddr in l:
                    found=True
                
    header_csv = header_csv[:-1]

def stats_pagemap(maps_frames, args):

    total_frames = 0
    total_pages = 0
    max_occurrences = 0
    for k,v in maps_frames.items():
        
        if int(k) != 0:
            total_frames += 1
            # do not consider 0x0 addresses
            if max_occurrences < len(v):
                max_occurrences = len(v)

        if args.verbose:
            print("0x%x" % k)
        
        for item in v:
            if args.verbose:
                print("\t0x%x" % item.virtual_address)
            total_pages += 1

    if args.short:
        prefix=""
        if args.mbqemu > 0:
            prefix = str(args.mbqemu)

        print("%.3f;%d" % ((float)(total_frames*PAGE_SIZE)/TO_MB, total_frames))
    else:
        print("Total Number of pages: {} ".format(total_pages) )
        print("Total Frames (in main memory): {}".format(total_frames))
        print("Memory used in frames: %d (Bytes) - %d (KiB) - %.3f (MiB)" % (total_frames*PAGE_SIZE, total_frames*PAGE_SIZE/1024, (float)(total_frames*PAGE_SIZE)/TO_MB))
        print("Max occurrences: {}".format(max_occurrences))

######################################################################

# str2bool is used for boolean arguments parsing.
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def get_ps_infos(output):
    processes = list()
    for s in output.split("\n"):
        if "-m" in s and "liftoff" not in s:
            processes.append(Process(s))
        
    return processes

def aggregate_to_csv(processes, args):

    maps_total_values = dict()
    for process in processes:
        
        for k,v in process.maps_key.items():
            if v.isdigit():
                if k not in maps_total_values:
                    maps_total_values[k] = int(v)
                else:
                    maps_total_values[k] += int(v)
    
    maps_total_values["pids"] = len(processes)
    now = datetime.now()
    needs_header=False
    
    # read csv
    if os.path.exists(args.csv):
        with open(args.csv, "r") as f:
            lines = f.read()
            if len(lines) == 0:
                needs_header=True
    else:
        needs_header=True

    # write csv
    buf = now.strftime("%H_%M_%S") + "," +  str(maps_total_values["pids"]) + "," #%d_%M_%Y_
    with open(args.csv, "a") as f:
        if needs_header:
            f.write(header_csv + "\n")
        
        for k,v in maps_total_values.items():
            buf += str(v) + "," 
        f.write(buf[:-1]+ "\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--process', help='Process to monitor', type=str, required=True)
    parser.add_argument('-s', '--short', help='Short display', type=str2bool, nargs='?', const=True, default=False)
    parser.add_argument('-v', '--verbose', help='Verbose Mode', type=str2bool, nargs='?', const=True, default=False)
    parser.add_argument('--usevm', help='Consider only qemu vm. It allows to consider only VMA_MERGEABLE AREA', type=str2bool, nargs='?', const=True, default=True)
    parser.add_argument('--pagemap', help='Stats entries via pagemap', type=str2bool, nargs='?', const=True, default=False)
    parser.add_argument('--smap', help='Stats entries via smap', type=str2bool, nargs='?', const=True, default=True)
    parser.add_argument('--csv', help='csv file', type=str, default=OUT_CSV)
    args = parser.parse_args()

    # Get the infos (pid + memory) of the given process(es)
    #try:
    output = subprocess.check_output("ps -aux | grep {}".format(args.process), shell=True)
    output = output.decode("UTF-8")
    if len(output) == 0:
        sys.exit('No process {} was found'.format(args.process))
    #except:
    #    sys.exit("No " +  args.process + " process")

    processes = get_ps_infos(output)
    if len(processes) == 0:
        sys.exit('No info associated to this process')
   
    # Get the mapping via /proc/$(pid)/maps and get the physical addresses
    maps_frames = defaultdict(list)
    for process in processes:
        read_maps(process,maps_frames, args)
        if args.smap:
            process_smap(process, args)

    if args.smap:
        aggregate_to_csv(processes, args)

    if args.pagemap:
        stats_pagemap(maps_frames, args)
                
if __name__ == "__main__":
    main()
