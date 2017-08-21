import argparse
import os
import re
import sys
def dispaly_error(message):
   FAIL = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   ENDC = '\033[0m'
   print FAIL + BOLD + UNDERLINE + message + ENDC

def collect_data(func, mes1, mes2):
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
                    print line
             
       else: 
        func(mes2)       
        sys.exit(1)
   else:
     func(mes1)
     parser.print_help()
     print "Aborting ..."


def main():
 message_error1 = "This python script takes exactly two arguments \n "
 message_error2 = "Please check the file path"
 collect_data(dispaly_error, message_error1, message_error2)

if __name__ == "__main__":
 main()

