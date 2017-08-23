import subprocess
import argparse
import os
import sys

FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'

def display_error(message):
   print FAIL + BOLD + UNDERLINE + message + ENDC
def display_result(message):
   print OKGREEN +  BOLD + message + ENDC
def vagrant_setup(func1, func2, mes1, mes2, mes3, mes4, mes5, mes6, mes7):
            
   parser = argparse.ArgumentParser(description='This Python script sets up a linux virtual machine and provision it')
   parser.add_argument('-v', '--vagrantfile', required=True, help='The relatif path of the vagrantfile')
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
        func1(mes1)       
        sys.exit(1)
      if args.scriptfile:
       if args.type is None:
         func1(mes4)
         sys.exit(1)
       if os.path.isfile(args.scriptfile):        
         subprocess.call(["sudo", "vagrant", "scp", args.scriptfile, "/home/vagrant"])
         func2(mes6)
         subprocess.call(["sudo", "vagrant", "ssh", "-c", args.type + " "+ args.scriptfile])
       else:
         func1(mes2)      
         sys.exit(1)
      if args.commandline:
        func2(mes7)                            
        subprocess.call(["sudo", "vagrant", "ssh", "-c", args.commandline])
    else:
        func1(mes3)
        sys.exit(1) 
   else: 
    func1(mes5)
    parser.print_help()
    print "Aborting ..."

def main():
 message_error1 = "Vagrantfile is not a file, please check vagrantfile path"
 message_error2 = "Scriptfile is not a file, please check scriptfile path"
 message_error3 = "Enter the path to your vagrantfile"
 message_error4 = "Specify the type of the script to invoke"
 message_error5 = "This python script takes at least two arguments \n "
 message_result1 = "** Script execution result **"
 message_result2 =  "** Command execution result **"
 vagrant_setup(display_error, display_result, message_error1, message_error2, message_error3, message_error4, message_error5, message_result1, message_result2)

if __name__ == "__main__":
 main()

