import os
from os.path import isfile, join
import argparse
import re

def processfile():
 word_dict = {}
 parser = argparse.ArgumentParser(description='This Python script processe files')
 parser.add_argument('-d', '--directory', required=True, help='folder path')
 args = parser.parse_args()
 for filename in os.listdir(args.directory):
  if isfile(join(args.directory, filename)): 
   filepath = join(args.directory, filename)
   fd = open(filepath, 'r')
   for line in fd.readlines():      
    word_list = line.split(' ')       
    word_dict.update({ word_list[0]: word_list[1] })
   print  word_dict 

def main():
 processfile()
if __name__ == "__main__":
 main()

