import subprocess
import sys
import argparse

def system_info():
 command = "dmidecode"
 parser = argparse.ArgumentParser(description="Python 'dmidecode' clone")
 parser.add_argument("-t", "--table", help="Extract hardware information by reading data from the DMI tables")
 args = parser.parse_args()
 if args.table:
   print "Gathering %s information..." % args.table
   subprocess.call([command, "-t", args.table])
 else:
   print "enter the name of the hardware to check"
   parser.print_help()

def main():
 system_info()

if __name__ == "__main__":
 main()
~       
