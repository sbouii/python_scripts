import gi
gi.require_version('Notify', '0.7')
import os
import re
import subprocess
from gi.repository import Notify

def desktop_notification(message):
 Notify.init('Failed_ssh_notification')
 Notify.Notification.new(message).show()

def logs_notification(func, mes1):
 line_regex = r".sshd.\d+...Failed"
 logging_filename= "/var/log/auth.log"
 subprocess.call(['sudo', 'chmod', '777', logging_filename])
 with open(logging_filename, "r") as f:
  for line in f:
    if re.search(line_regex, line, re.M|re.I):
      func(mes1)

def main():
 message = "There are SSH Errors occured on the server, check the /var/log/auth.log for further informations"
 logs_notification(desktop_notification, message)
 
if __name__ == "__main__":
 main()

