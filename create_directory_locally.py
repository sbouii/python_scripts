import os

directory_name = raw_input("Enter the name of the directory to create: ")
path_name = os.path.basename(directory_name)
current_directory = os.getcwd() 

if not os.path.exists(path_name):
 os.makedirs(path_name)
 print "your current directory is: " + current_directory  + "the created directory is : " + path_name
else:
 print "Directory already exists"
