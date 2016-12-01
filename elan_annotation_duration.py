from __future__ import print_function
#from xml.etree import ElementTree as et
from datetime import timedelta
import os,sys
try:
    from xml.etree import cElementTree as et
except ImportError:
    from xml.etree import ElementTree as et

def get_file_signs(filename):
    '''Reads through the eaf-files collecting all timestamps and returning the 
    difference between the first and last stamp'''
    tree = et.parse(filename)
    time_stamps = []
    root = tree.getroot()
    for tier in root.iter("TIME_ORDER"):
        for timestamp in tier.iter("TIME_SLOT"):
            time_stamps.append(int(timestamp.attrib["TIME_VALUE"]))
    dur = max(time_stamps)-min(time_stamps)
    return dur

def get_all_signs(directory):
    '''Iterates over all eaf-files of a directory and prints the number of files found 
    and the total duration of the annotation span across all files'''
    dur = 0
    files = 0
    for filename in os.listdir(directory):
        if filename.endswith(".eaf"):
            files += 1
            filename = directory+"/"+filename
            file_dur = get_file_signs(filename)
            dur += file_dur
    print()
    print("Total number of files:",files)
    print("Total annotation span (h:m:s.ms):",str(timedelta(milliseconds=dur))[:-3])
    print()
    return dur

def main():
    '''Runs the iteration over all eaf-files in the same directory as the py-file'''
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = "."
    get_all_signs(directory) # Change the "." to the directory of your eaf-files (if other)

if __name__=='__main__':
    main()
