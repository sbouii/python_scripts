import os
import argparse

def processline(line):

 print line
 
def processfile(func1):
 parser = argparse.ArgumentParser(description='This Python script processe files')
 parser.add_argument('-d', '--directory', required=True, help='folder path')
 args = parser.parse_args()  
 for filename in os.listdir(args.directory):
  filepath = os.path.join(args.directory, filename)
  fd = open(filepath, 'r')
  for line in fd.readlines():
   func1(line)

def main():
 processfile(processline)
if __name__ == "__main__":
 main()
