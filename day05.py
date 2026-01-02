# file handling
# CRUD operation in file using python (a raw method to do this )
# File handling means reading data from files and writing data to files stored on disk.
'''
Text file    → strings → encoding
Binary file → bytes   → raw data

'''
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
data_file=f'{dir_path}/abc.txt'
print(data_file)
fs=open(data_file , 'r')
print(fs.read())

