import subprocess
import argparse
import os
import sys
import paramiko
from paramiko import SSHClient
def display_error(message):

   FAIL = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   ENDC = '\033[0m'
   print FAIL + BOLD + UNDERLINE + message + ENDC

def vagrant_setup(func, mes1, mes2, mes3, mes4, mes5):
            
   parser = argparse.ArgumentParser(description='This Python script sets up a linux virtual machine and provision it')
   parser.add_argument('-v', '--vagrantfile', help='The relatif path of the vagrantfile')
   parser.add_argument('-c', '--commandline', help='The command line to execute on the remote server, is an alternative for the scriptfile argument')
   parser.add_argument('-s', '--scriptfile', help='The path of the script to execute, is an alternative for the commandline argument')
   parser.add_argument('-t', '--type', help='the type of the script to type')
   args = parser.parse_args()
    
   if len(sys.argv) >= 4:
    subprocess.call(["sudo", "vagrant", "plugin", "install", "vagrant-scp"])
    if args.vagrantfile:
      if os.path.isfile(args.vagrantfile):
        subprocess.call(["mv", "vagrantfile", "./"])
        subprocess.call(["sudo", "vagrant", "up", "--provision"])        
      else:       
        func(mes1)       
        sys.exit(1)
      if args.scriptfile:
       if args.type is None:
         func(mes4)
         sys.exit(1)
       if os.path.isfile(args.scriptfile):        
         subprocess.call(["sudo", "vagrant", "scp", args.scriptfile, "/home/vagrant"])
         subprocess.call(["sudo", "vagrant", "ssh", "-c", args.type + " "+ args.scriptfile])
       else:
         func(mes2)      
         sys.exit(1)
      if args.commandline:                    
        subprocess.call(["sudo", "vagrant", "ssh", "-c", args.commandline])
    else:
        func(mes3)
        sys.exit(1) 
   else: 
    func(mes5)
    parser.print_help()
    print "Aborting ..."

def main():
 message_error1 = "Vagrantfile is not a file, please check vagrantfile path"
 message_error2 = "Scriptfile is not a file, please check scriptfile path"
 message_error3 = "Enter the path to your vagrantfile"
 message_error4 = "Specify the type of the script to invoke"
 message_error5 = "This python script takes at least two arguments \n "
 vagrant_setup(display_error, message_error1, message_error2, message_error3, message_error4, message_error5)

if __name__ == "__main__":
 main()

