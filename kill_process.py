import argparse
import subprocess
import sys
FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'
def display_error(message):
   print FAIL + BOLD + UNDERLINE + message + ENDC
def display_result(message):
   print OKGREEN + BOLD + message + ENDC
def process_action(func1,func2, mes1, mes2, mes3):
   parser = argparse.ArgumentParser(description='This Python script collects data from files')
   parser.add_argument('-p', '--process', nargs='+', type=str, required=True, help='The name of the process')
   args = parser.parse_args()
   if len(sys.argv) < 7:
     if args.process:
      for i in args.process:       
       output = subprocess.Popen(['pidof', i], stdout=subprocess.PIPE).communicate()[0] 
       process_id = [str(i) for i in output.split()]             
       if process_id: 
        for i in process_id:         
          process = subprocess.call(["kill", "-9", i])
        func2(mes2)
        print args.process
       else:
        func1(mes2)
        sys.exit(1)
                                    
      func2(mes3)
      print args.process
   else:
     func1(mes1)
     parser.print_help()
     print "Aborting ..."

def main():
 message_error1 = "This python script takes at least two arguments \n "
 message_error2 = "There is no process with this name, check the process name"
 message_result = "*** killed process ***\n"
 process_action(display_error,display_result, message_error1, message_error2, message_result)

if __name__ == "__main__":
 main()

