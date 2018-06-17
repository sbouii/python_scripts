import subprocess
import commands

FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'

def display_error(message):
  print FAIL + BOLD + UNDERLINE + message + ENDC

def display_result(message):
  print OKGREEN + BOLD + message + ENDC

def check_process_status(func1, func2, mes1, mes2):
   process = raw_input("Enter the name of the process to check: ")
#  try:
   output = commands.getoutput("ps -f|grep " + process)

   processinfo = output.split()
   func2(mes2)
   print "\n\
   Full path:\t\t", processinfo[5], "\n\
   Owner:\t\t", processinfo[0], "\n\
   Process ID:\t\t", processinfo[1], "\n\
   Parent process ID:\t", processinfo[2], "\n\
   Time started:\t", processinfo[4]  
#  except:
#   func1(mes1)
def main():
 message_error1 = "There is no process with this name" 
 message_result = "*** Process status: ***"
 check_process_status(display_error, display_result, message_error1, message_result)
if __name__ == "__main__":
 main() 
