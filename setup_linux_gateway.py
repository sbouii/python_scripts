import subprocess
import argparse
import os
import sys
def vagrant_setup():
  parser = argparse.ArgumentParser(description='This Python script sets up a linux virtual machine as gateway')
  parser.add_argument('-v', '--vagrantfile', help='The relatif path of the vagrantfile')
  parser.add_argument('-c', '--commandline', help='The command line to execute on the remote server')
  parser.add_argument('-s', '--scriptfile', help='The path of the script to execute')

  args = parser.parse_args()
  if len(sys.argv) == 3:
    if args.vagrantfile:
      if os.path.isfile(args.vagrantfile):
        subprocess.call(["mv", "vagrantfile", "./"])
        subprocess.call(["sudo", "vagrant", "up", "--provision"])
        subprocess.call(["sudo", "vagrant", "ssh"])

      else:
        dispaly_error("Vagrantfile is not a file, please check vagrantfile path")       
        sys.exit(1)
    if args.scriptfile :
      if os.path.isfile(args.scriptfile):
        subprocess.call([args.scriptfile])          
      else:
        dispaly_error("Scriptfile is not a file, please check scriptfile path")         sys.exit(1)
    elif args.commandline:
       dispaly_error("Enter a scriptfile or a commandline")
       sys.exit(1)
    else: 
      if args.commandline:
        subprocess.call([args.commandline])   
  else: 
   print "This python script takes exactly two arguments \n "
   parser.print_help()
   print "Aborting ..."

def main():
 vagrant_setup()

if __name__ == "__main__":
 main()


