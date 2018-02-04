import socket
import os, sys
import subprocess
import psutil
import argparse
import psutil
def scan_ports():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(('INSERT SOME TARGET WEBSITE.com', 'ANY PORT'))
  s.connect(("8.8.8.8", 80))
  ip_address = s.getsockname()[0]
  print "Scanning ports on the machine ", ip_address
  print "-" * 44
  try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

  except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

  except socket.gaierror:
    print "Couldn't resolve ip address. Exiting"
    sys.exit()

  except socket.error:
    print "Couldn't connect to server. Exiting"
    sys.exit()

def main():
 
 scan_ports()

if __name__ == "__main__":
 main()
