#!/usr/bin/python3
import os
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

TYPE_FILE = ["vanilla.json", "terry.json", "gaulthier.json"]
#TYPE_FILE = ["vm.json", "heap.json", "unikernel.json"]
EXT = ".json"

WORKDIR = '/home/terrylos/Thesis/thesis/ASLR-Dedu/test10images/Data'
FOLDER  = 'plot'

FRAMES      = "frames"
RATIO       = "ratio"

SHARED      = "pages_shared"
SHARING     = "pages_sharing"
UNSHARED    = "pages_unshared"
VOLATILE    = "pages_volatile"

KEY = FRAMES
CSV_FILE="min.csv"

FILENAME=WORKDIR + FOLDER + "_" + KEY

AGG     = True
MEM     = False

PAGES_INDEX = 0
TIME_INDEX  = 1
STOP        = 1200
START       = 20

VM          = 5
BASE_REPR   = 1024
PAGE_SIZE   = 4096
VMA_SIZE    = 0xa00000

class JsonFile:
    def __init__(self, name, filepath, folder):
        self.name = name
        self.filepath = filepath
        self.folder = folder
        self.content = None
        self.min_values = 0

class Data:
    def __init__(self, folder):
        self.pages_values = defaultdict(list)
        self.time_values  = defaultdict(list)
        self.folder = folder
        

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def process_folder(args):
    
    list_files = [None, None, None]
    for f in os.listdir(args.workdir):
        
        if f.endswith(EXT):
            json_file = JsonFile(f, os.path.join(args.workdir, f), args.workdir.split("/")[-1])
            with open(json_file.filepath, 'r') as fp:
                print(json_file.filepath)
                json_file.content = json.load(fp)   



            if args.typefile[0] in f:
                list_files[0] = json_file
            elif len(args.typefile) > 1 and args.typefile[1] in f:
                list_files[1] = json_file
            elif len(args.typefile) > 2 and args.typefile[2] in f:
                list_files[2] = json_file
            elif len(args.typefile) > 3 and args.typefile[3] in f:
                list_files[3] = json_file
            elif len(args.typefile) > 4 and args.typefile[4] in f:
                list_files[4] = json_file
            elif len(args.typefile) > 5 and args.typefile[5] in f:
                list_files[5] = json_file
            else:
                print("[WARNING] Unknown file: %s" %f)
    print(list_files)
    return list_files

def process_file_data(data, json_file, args):

    field = json_file.name
    t0 = 0

    if args.memory:
        to_mb = (BASE_REPR*BASE_REPR)
        vma_size = (args.vmasize/args.pagesize)
        cons_all = vma_size*args.nbvm
    
    ksm_data = json_file.content
    for i, p in enumerate(ksm_data[SHARING]):
        
        if i >= args.stop:
            continue

        if SHARING == args.key:
            
            if args.memory:
                i1 = (float)(cons_all*args.pagesize)/to_mb
                i2 = (float)(p[PAGES_INDEX]*args.pagesize)/to_mb
                data.pages_values[field].append(i1-i2)
            else:
                data.pages_values[field].append(p[PAGES_INDEX])

        elif FRAMES == args.key:
            
            s = ksm_data[SHARED][i]
            u = ksm_data[UNSHARED][i]
            if VOLATILE in ksm_data:
                v = ksm_data[VOLATILE][i]
                total = s[PAGES_INDEX] + u[PAGES_INDEX] + v[PAGES_INDEX]
            else:
                total = s[PAGES_INDEX] + u[PAGES_INDEX]
                
            if args.memory:
                data.pages_values[field].append((total*args.pagesize)/to_mb)
            else:
                data.pages_values[field].append(total)

        elif RATIO == args.key:
            
            # Unshared / sharing:
            #   The higher it is, the worse it is
            sharing = ksm_data[SHARING][i]
            u = ksm_data[UNSHARED][i]

            if sharing[PAGES_INDEX] == 0:
                ratio = 0
            else:
                ratio = float(u[PAGES_INDEX]/sharing[PAGES_INDEX])

            data.pages_values[field].append(ratio)

        
        if i == 0:
            data.time_values[field].append(0)
            t0 = p[TIME_INDEX]
        else:
            data.time_values[field].append(p[TIME_INDEX]-t0)

def annot_max(x,y, label, str_ymax, args):
    ymax = max(y[-3:])
    xpos = y.index(ymax)
    xmax = x[xpos]
    if args.memory or args.key == RATIO:
        str_ymax += "{}: {:.2f}MB - ".format(label, ymax)
    else:
        str_ymax += "{}: {} - ".format(label, ymax)
    return str_ymax
    
def draw_plot(data, args):
    
    labels = []
    if "_pie.json" in args.typefile:
        labels = ["pie", "unaligned", "aligned"]
    elif "_local_align.json" in args.typefile:
        labels  = ["vanilla", "1 ind", "n ind"]
    else:
        labels  = ["vanilla", "global table", "append table"]
        
    colors  = ["#1f77b4", "#ff7f0e", "#2ca02c", "#66f542", "#a02c51", "#63ada6"]
    lines   = ["-", ':', '-.', '--', '-', '-.']

    str_ymax = ""
    if args.aggregate:
        fig, ax = plt.subplots()
        for i, field in enumerate(args.typefile):
            ax.plot(data.time_values[field], data.pages_values[field], label=labels[i], linestyle=lines[i])
            if len( data.pages_values[field]) > 0:
                str_ymax = annot_max(data.time_values[field],data.pages_values[field], labels[i], str_ymax, args)
        
        ax.tick_params(labeltop=False, labelright=True)
        ax.annotate(str_ymax[:-2], xy=(0, 1), xycoords='axes fraction', fontsize=8,
                horizontalalignment='left', verticalalignment='bottom')
        if args.memory:
            ax.set(xlabel='Time [s]', ylabel='Memory used [MB]')
        elif args.key == FRAMES:
            ax.set(xlabel='Time [s]', ylabel='# Frames used')
        elif args.key == SHARING:
            ax.set(xlabel='Time [s]', ylabel='# Pages sharing')
        elif args.key == RATIO:
            ax.set(xlabel='Time [s]', ylabel='Ratio (unshared/sharing)')

        ax.legend()
        ax.grid()

        if args.ymax:
            #plt.ylim(ymin=0)
            #plt.xlim(xmin=0)
            ax.margins(0)
            plt.yticks(np.arange(0, args.ymax+1, args.ystep))
            
        if args.xmax:
            plt.xticks(np.arange(0, args.xmax+1, args.xstep))
        
    else:
        fig, t = plt.subplots(len(args.typefile))
        for i, field in enumerate(args.typefile):
            t[i].plot(data.time_values[field], data.pages_values[field], label=labels[i], color=colors[i])
            t[i].grid()
            t[i].legend()
            if args.memory:
                t[i].set(xlabel='Time [s]', ylabel='Memory used [MB]')
            elif args.key == FRAMES:
                t[i].set(xlabel='Time [s]', ylabel='# Frames used')
            elif args.key == SHARING:
                t[i].set(xlabel='Time [s]', ylabel='# Pages sharing')
            elif args.key == RATIO:
                t[i].set(xlabel='Time [s]', ylabel='Ratio (unshared/sharing)')
        #plt.setp(t, yticks=np.arange(0, args.ymax+1, args.ystep))
        #plt.setp(t, xticks=np.arange(0, args.xmax+1, args.xstep))

    filename = args.filename
    if args.memory:
        filename = os.path.splitext(filename)[0]
        filename += "_memory"

    if "." not in filename:
        filename += ".pdf"

    plt.savefig(filename, bbox_inches='tight')
    print("Image saved to: " + filename)
    plt.legend()

    if args.display:
        plt.show()

def save_min_values(alljsonfiles, args):
    f = open(os.path.join(args.workdir,CSV_FILE), "a")

    if os.stat(os.path.join(args.workdir,CSV_FILE)).st_size == 0:
        csv_string = "folder;vanilla;terry;gaulthier\n"
        f.write(csv_string)
    
    if args.memory:
        csv_string = alljsonfiles[0].folder + "_memory;"
    else:
        csv_string = alljsonfiles[0].folder + "_frames;"
    
    for i, json_file in enumerate(alljsonfiles):
        csv_string += str(json_file.min_value)
        if i < len(alljsonfiles) -1:
            csv_string += ";"
    csv_string += "\n"
    f.write(csv_string)
    f.close()

def find_min_values(data, json_file):

    min_array = list()
    total_lenght= len(data.pages_values[json_file.name])
    for i, element in enumerate(data.pages_values[json_file.name]):
        if i > total_lenght-100 and i < total_lenght-20:
             min_array.append(element)
    json_file.min_value = min(min_array)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--workdir', help='Path to json file to plot (default = merged.json)', type=str, 
        default=os.path.join(WORKDIR, FOLDER))
    parser.add_argument('-a', '--aggregate', help='Aggregate in one plot', type=str2bool, nargs='?', const=True, default=AGG)
    parser.add_argument('-n', '--nbvm', help='Number of VM (default = 10)', type=int, default=VM)
    parser.add_argument('-v', '--vmasize', help='Size of the VM in hex (default = 0xa00000)', type=str, default=VMA_SIZE)
    parser.add_argument('-p', '--pagesize', help='Page size (default = 4096)', type=int, default=PAGE_SIZE)
    parser.add_argument('-s', '--stop', help='Stop the graph after s seconds', type=int, default=STOP)
    parser.add_argument('-m', '--memory', help='Display graph with memory (MiB)', type=str2bool, nargs='?', const=True, default=MEM)
    parser.add_argument('-k', '--key', help='Key of ksm to analyse', default=KEY)
    parser.add_argument('-d', '--display', help='Display the plot', type=str2bool, nargs='?', const=True, default=True)
    parser.add_argument('-f', '--filename', help='Absolute filename of the image', default=FILENAME)
    parser.add_argument('-t', '--typefile', help="list of files to merge (as a list)" , nargs='+', type=str, default=TYPE_FILE)

    parser.add_argument('--ymax', help='Max value for y axis', type=int)
    parser.add_argument('--ystep', help='Step value for y axis', type=int)
    
    parser.add_argument('--xmax', help='Max value for x axis', type=int)
    parser.add_argument('--xstep', help='Step value for x axis', type=int)
    

    args = parser.parse_args()
    json_files = process_folder(args)
    
    data = Data(json_files[0].folder)
    
    for json_file in json_files:
        process_file_data(data, json_file, args)
        find_min_values(data, json_file)

    draw_plot(data, args)
    if args.key == FRAMES:
        save_min_values(json_files, args)
  
if __name__== "__main__":
    main()  
