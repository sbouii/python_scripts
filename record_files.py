import os
path = raw_input("Enter the path of the directory to record files inside it: ")
fd = open('record_file', "w")
for dirpath, dirname, filenames in os.walk(path):
 for filename in filenames:
  fd.write(os.path.abspath(filename))
   
