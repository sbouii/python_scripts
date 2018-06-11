import os
from os.path import isfile, join
import argparse
import re
 
def processfile():
 parser = argparse.ArgumentParser(description='This Python script processe files')
 parser.add_argument('-d', '--directory', required=True, help='folder path')
 args = parser.parse_args()
 for filename in os.listdir(args.directory):
  if isfile(join(args.directory, filename)):
   filepath = join(args.directory, filename)
   fd = open(filepath, 'r')
   print "File: " + filename + "\n"
   list_file = []
   for line in fd.readlines():
    line_regex = r"^test"
    if re.search(line_regex, line, re.M):
     list_file.append(line)
   print list_file 
def main():
 processfile()
if __name__ == "__main__":
 main()


