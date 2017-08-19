import sys
import subprocess
import argparse
def system_info():
   command = "uname"
 
   parser = argparse.ArgumentParser(description='Python uname command')
   parser.add_argument('-s', '--name', action='store_true', help='print the kernel name')
   parser.add_argument('-n', '--nodename', action='store_true', help='print the network node hostname')
   parser.add_argument('-r', '--release', action='store_true', help='print the kernel release')
   parser.add_argument('-v', '--version', action='store_true', help='print the version')
   parser.add_argument('-m', '--machine', action='store_true', help='print the machine hardware name')
   parser.add_argument('-p', '--processor', action='store_true', help='print the processor type')
   parser.add_argument('-i', '--hardwareplatform', action='store_true', help='print the hardware platform')
   parser.add_argument('-o', '--operatingsystem', action='store_true', help='print the operating system')
   parser.add_argument('-a', '--all', action='store_true', help='print all information ')
   args = vars(parser.parse_args())
   if len(sys.argv) == 2:
    if args['name']:
      print "Gathering the kernel name ..."
      subprocess.call([command, "-s"])

    if args['nodename']:
      print "Gathering the nodename ..."
      subprocess.call([command, "-n"])

    if args['release']:
      print "Gathering the kernel-release ..."
      subprocess.call([command, "-r"])

    if args['version']:
      print "Gathering the kernel version ..."
      subprocess.call([command, "-v"])
  
    if args['machine']:
      print "Gathering the machine hardware name ..."
      subprocess.call([command, "-m"])
  
    if args['processor']:
      print "Gathering the processor type"
      subprocess.call([command, "-p"])

    if args['hardwareplatform']:
      print "Gathering informations about the hardware platform ..."
      subprocess.call([command, "-i"])

    if args['operatingsystem']:
      print "Gathering informations about the operating system ..."
      subprocess.call([command, "-o"])
   else:
    print "%s command_line takes one argument at once \n " % command
    parser.print_help()

def main():
 system_info()

if __name__ == "__main__":
 main()
 
