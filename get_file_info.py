import os
import time
# stat module defines constants and functions for interpreting the result of os.stat()
import stat 

file_name = raw_input("Enter the file name:")
if os.path.exists(os.path.abspath(file_name)):
 fd = open(file_name, "r") 
 nb_lines = 0
 for line in fd:
  nb_lines = nb_lines + 1
 file_stat = os.stat(file_name)
 file_stat_dict = {
     'file_absolute_path': os.path.abspath(file_name),
     'file_owner_id': file_stat[stat.ST_UID],
     'file_group_owner_id': file_stat[stat.ST_GID],
     'file_number_hardlinks': file_stat[stat.ST_NLINK],
     'file_recent_access_time': time.strftime("%d/%m/%Y %I:%M:%S %p",
time.localtime(file_stat[stat.ST_ATIME])),
     'file_recent_content_modification_time': time.strftime("%d/%m/%Y %I:%M:%S %p",
time.localtime(file_stat[stat.ST_MTIME])),
     'file_recent_metadata_modification_time': time.strftime("%d/%m/%Y %I:%M:%S %p",
time.localtime(file_stat[stat.ST_CTIME])), 
     'file_size_bytes': file_stat[stat.ST_SIZE],
     'number_lines': nb_lines,
     'file_permessions': file_stat[stat.ST_MODE],
     'file_device':  file_stat[stat.ST_DEV]
     
 }
 
 print "file absolute path : " + str(file_stat_dict['file_absolute_path']) + "\n"
 print "file owner id : " + str(file_stat_dict['file_owner_id']) + "\n"
 print "file group owner id : " + str(file_stat_dict['file_group_owner_id']) + "\n"
 print "file number of hardlinks : " + str(file_stat_dict['file_number_hardlinks']) + "\n"
 print "recent access time : " +  file_stat_dict['file_recent_access_time'] + "\n"
 print "recent content modification time : " +  file_stat_dict['file_recent_content_modification_time'] + "\n"
 print "file recent metadata modification time : " + file_stat_dict['file_recent_metadata_modification_time'] + "\n"
 print "file size in bytes : " + str(file_stat_dict['file_size_bytes']) + "\n"
 print "number of lines : " + str(file_stat_dict['number_lines']) + "\n"
 print "file permessions : " + str(file_stat_dict['file_permessions']) + "\n"
 print "file device : " +  str(file_stat_dict['file_device']) + "\n"

 
else:
 print "File doesn't exist" 
