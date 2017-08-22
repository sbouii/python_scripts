import argparse
import os
import re
import sys

FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'

def dispaly_error(message):   
   print FAIL + BOLD + UNDERLINE + message + ENDC
def display_message(message):
   print OKGREEN + BOLD + UNDERLINE + message + ENDC
def collect_data(func1, func2, mes1, mes2, mes3):
   parser = argparse.ArgumentParser(description='This Python script collects data from files')
   parser.add_argument('-f', '--file', required=True, help='The relatif path of the file to collect data from')
   parser.add_argument('-w', '--word', type=str, required=True, help='The word to use for searching related data')
   args = parser.parse_args()
   if len(sys.argv) == 5:
     if args.file:
       if os.path.isfile(args.file):
          with open(str(args.file), 'r') as f:
            for line in f:
               if re.search(args.word, line, re.M|re.I):
                    func2(mes3)
                    print line
                       
       else: 
        func1(mes2)       
        sys.exit(1)
   else:
     func1(mes1)
     parser.print_help()
     print "Aborting ..."


def main():
 message_error1 = "This python script takes exactly two arguments \n "
 message_error2 = "Please check the file path"
 message_result = "Collected data"
 collect_data(dispaly_error, display_message, message_error1, message_error2, message_result)

if __name__ == "__main__":
 main()

