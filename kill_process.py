import argparse
import subprocess
import sys
FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'
def dispaly_error(message):
   print FAIL + BOLD + UNDERLINE + message + ENDC
def display_result(message):
   print OKGREEN + BOLD + message + ENDC
def process_action(func1,func2, mes1, mes2):
   parser = argparse.ArgumentParser(description='This Python script collects data from files')
   parser.add_argument('-p', '--process', nargs='+', type=str, required=True, help='The name of the process')
   parser.add_argument('-a', '--action', nargs='?', help='The action to take on the process')
   args = parser.parse_args()
   if len(sys.argv) < 5:
     if args.process:
      for i in args.process:       
       output = subprocess.Popen(['pidof', i], stdout=subprocess.PIPE).communicate()[0] 
       process_id = [str(i) for i in output.split()]      
             
       if process_id is None:
        func1(mes2)
        sys.exit(1)
       else: 
        for i in process_id:         
          process = subprocess.call(["kill", "-9", i])
                                    
      func2(mes2)
      print args.process
   else:
     func1(mes1)
     parser.print_help()
     print "Aborting ..."

def main():
 message_error = "This python script takes at least two arguments \n "
 message_error = "There is no process with this name, check the process name"
 message_result = "*** killed process ***\n"
 process_action(dispaly_error,display_result, message_error, message_result)

if __name__ == "__main__":
 main()

