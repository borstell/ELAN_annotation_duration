# ELAN_annotation_duration
Tool that counts the total duration of the annotated ELAN annotation files (`.eaf`) in a folder
## Usage
  1. Save the file `elan_annotation_duration.py` onto your computer (NB: Python 2.x or higher is required).
  2. 
  a. (simple) If the `.py` file is in the same folder as your `.eaf` files, run the `.py` file by clicking it.
  
  b. (advanced) If you run the `.py` file through the command line, you have the option of specifying the location of your directory with `.eaf` files manually as an additional argument (see below).
  
## Command-line
Simple:
```
python3 elan_annotation_duration.py
Total number of files: 105
Total annotation span (h:m:s.ms): 7:56:13.391
```
With specified folder location:
```
python3 elan_annotation_duration.py /home/my_computer/my_elan_files
Total number of files: 105
Total annotation span (h:m:s.ms): 7:56:13.391
```
This output shows that we have 105 `.eaf` files in our folder, and that the total span from the start of the first annotation cell to the end of the last annotation cell across all files is 7 hours, 56 minutes, 13 seconds, and 391 milliseconds.
