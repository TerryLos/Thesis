#!/usr/bin/python3
from collections import defaultdict
import os
import numpy as np
import argparse
import matplotlib.pyplot as plt

TYPE_FILE = ["aslr_terry.csv","aslr_gaulthier.csv","vanilla.csv"]
EXT = ".csv"

WORKDIR = '/Users/gaulthiergain/Desktop/memory_dedup/unikernels_data/sharing'
FOLDER  = '100lambda'

FILENAME="/Users/gaulthiergain/Desktop/memory_dedup/figs/unikernels/sharing/smap_mem/" + FOLDER

INDEX=6
CSV_FILE="min_smap.csv"

class CSVFile:
    def __init__(self, name, filepath):
        self.name = name
        self.filepath = filepath
        self.content = None
        self.data = list()
        self.folder = filepath.split("/")[-1]
        self.min_values = 0

class Data:
    def __init__(self):
        self.fields = list()
        self.data_time = None
        self.data = defaultdict(list)
        
def save_min_values(allcsvFiles, args):
    f = open(os.path.join(args.workdir,CSV_FILE), "w")

    if os.stat(os.path.join(args.workdir,CSV_FILE)).st_size == 0:
        csv_string = "folder;DCE;unaligned;aligned;_aslr_dce;_aslr_default;_aslr_plt\n"
        f.write(csv_string)
    
    csv_string = allcsvFiles[0].folder + "_memory;"
    
    for i, json_file in enumerate(allcsvFiles):
        csv_string += str(json_file.min_value)
        if i < len(allcsvFiles) -1:
            csv_string += ";"
    csv_string += "\n"
    f.write(csv_string)
    f.close()

def find_min_values(data, csv_file):

    min_array = list()
    total_lenght= len(data.data[csv_file.name])
    for i, element in enumerate(data.data[csv_file.name]):
        if i > total_lenght-50 and i < total_lenght-20:
            min_array.append(element)
    csv_file.min_value = min(min_array)

def plot(data, args):
    labels  = ["Global table", "Append table", "Vanilla"]  
    #colors  = ["#E89C52","#5FB7E4","#97C159","#a02c51", "#1f77b4", "#ff7f0e", "#2ca02c", "#66f542", "#a02c51", "#63ada6"]
    lines   = ["-", '-', '-', '-.', '-.', '-.']

    fig, ax = plt.subplots()
    for i, field in enumerate(data.fields):
        ax.plot(data.data[field], label=labels[i], linestyle=lines[i])#, color=colors[i])
    
    ax.set(xlabel='Time [s]', ylabel='Memory used [MB]')
    plt.grid()
    plt.legend()

    filename = args.filename
    if "." not in filename:
        filename += ".pdf"

    #plt.yticks(np.arange(0, 250+1,25)) for 100uk
    plt.savefig(filename, bbox_inches='tight')
    print("Image saved to: " + filename)
    plt.legend()

    if args.display:
        plt.show()

def process_file(data, csv_file, max_length, args):
    
    if max_length < len(csv_file.content):
        max_length = len(csv_file.content)
        data.data_time = list(range(0, max_length))
    
    for i, content in enumerate(csv_file.content):
        if i == 0:
            #header
            continue
        sc = content.split(",")
        if "_local_align" in csv_file.name:
            print(int(sc[INDEX]), end=" : ")
            print(int(sc[INDEX])/1024)

        csv_file.data.append(int(sc[INDEX])/1024)
        if i > 60:
            break
    
    data.fields.append(csv_file.name)
    data.data[csv_file.name] = csv_file.data

def process_folder(args):
    
    list_files = [None, None, None]
    for f in os.listdir(args.workdir):
        
        if f.endswith(EXT):
            
            csv_file = CSVFile(f, os.path.join(args.workdir, f))
            with open(csv_file.filepath, 'r') as fp:
                csv_file.content = [l.rstrip("\n") for l in fp]

            if args.typefile[0] in f:
                list_files[0]= csv_file
            elif len(args.typefile) > 1 and args.typefile[1] in f:
                list_files[1]= csv_file
            elif len(args.typefile) > 2 and args.typefile[2] in f:
                list_files[2]= csv_file
            elif len(args.typefile) > 3 and args.typefile[3] in f:
                list_files[3]= csv_file
            elif len(args.typefile) > 4 and args.typefile[4] in f:
                list_files[4]= csv_file
            elif len(args.typefile) > 5 and args.typefile[5] in f:
                list_files[5]= csv_file

    return list_files

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--workdir', help='Path to csv file to plot', type=str, 
        default=os.path.join(WORKDIR, FOLDER))
    parser.add_argument('-t', '--typefile', help="list of files to merge (as a list)" , nargs='+', type=str, default=TYPE_FILE)
    parser.add_argument('-d', '--display', help='Display the plot', type=str2bool, nargs='?', const=True, default=True)
    parser.add_argument('-f', '--filename', help='Absolute filename of the image', default=FILENAME)

    parser.add_argument('--ymax', help='Max value for y axis', type=int)
    parser.add_argument('--ystep', help='Step value for y axis', type=int)
    
    parser.add_argument('--xmax', help='Max value for x axis', type=int)
    parser.add_argument('--xstep', help='Step value for x axis', type=int)

    args = parser.parse_args()
    csv_files = process_folder(args)

    max_length = 0
    data = Data()
    for csv_file in csv_files:
        process_file(data, csv_file, max_length, args)
        find_min_values(data, csv_file)
    
    plot(data, args)
    save_min_values(csv_files, args)

if __name__== "__main__":
    main()  
