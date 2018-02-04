import socket
import os, sys
import argparse
  
def scan_ports():
  parser = argparse.ArgumentParser(description='This Python script return if a specified port is open or not on a specified machine')
  parser.add_argument('-a', '--address', required=True, help='The ip address of the remote machine to scan')
  parser.add_argument('-p', '--port', required=True, help='The port on the remote machine ')
  args = parser.parse_args()
  if len(sys.argv) == 5:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((args.address, int(args.port)))
      s.shutdown(2)
      print "port %s is open" %args.port
   except:
      print "port %s is not open" %args.port
  else:
   print "you should enter exactly two arguments"
   parser.print_help()
   print "Aborting ..."
def main():
 scan_ports()
if __name__ == "__main__":
 main()
