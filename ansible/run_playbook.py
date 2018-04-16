import subprocess
import ansible.runner
import ansible.playbook
from ansible import callbacks
from ansible import utils
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
  print OKGREEN + BOLD + message + ENDC

def run_playbook(func1, func2, mes1, mes2, mes3):
  parser = argparse.ArgumentParser(description='This Python script runs ansible playbooks')
  parser.add_argument('-fa', '--fileplaybook', required=True, help='The relatif path of the ansible-palybook file')
  parser.add_argument('-fi', '--fileinventory', required=True, help='The relatif path of the inventory file')
  args = parser.parse_args()
  if len(sys.argv) == 5:
    if (args.fileplaybook and args.fileinventory):
        if os.path.isfile(args.fileplaybook) and os.path.isfile(args.fileplaybook):
             stats = callbacks.AggregateStats()
             playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
             runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)
             
             pb = ansible.playbook.PlayBook(playbook= args.fileplaybook, host_list = args.fileinventory , stats=stats, callbacks=playbook_cb, runner_callbacks=runner_cb, check=False)
             pb.run()
        else:
          func1(mes2)
          sys.exit(1)

  else:
     func1(mes1)
     parser.print_help()
     print "Aborting ..."

def main():
   message_error1 = "This python script takes exactly two arguments \n "
   message_error2 = "Please check the path of the playbook-ansible or of the inventory file"
   message_result = "*** Running ansible-playbook ***"

   run_playbook(display_error, display_result, message_error1,  message_error2, message_result)
   
if __name__ == "__main__":
  main()
