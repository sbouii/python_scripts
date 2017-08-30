import os
import re
import smtplib
import subprocess
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
def send(mail_from, mail_to, password):
 email = MIMEMultipart()
 email['From']=mail_from 
 email['To']=mail_to
 email['Subject']='SSH Error on the server'
 message = 'There are SSH Errors occured on the server, check the /var/log/auth.log for further informations'
 email.attach(MIMEText(message))
 mailserver = smtplib.SMTP('smtp.gmail.com', 587)
 mailserver.ehlo()
 mailserver.starttls()
 mailserver.ehlo()
 mailserver.login(mail_from, password)
 mailserver.sendmail(mail_from, mail_to, email.as_string())
 mailserver.quit()
def logs_notification(func, mail1, mail2, psw):
 line_regex = r".sshd.\d+...Failed"
 logging_filename= "/var/log/auth.log"
 subprocess.call(['sudo', 'chmod', '777', logging_filename])
 with open(logging_filename, "r") as f:
  for line in f:
   if re.search(line_regex, line, re.M|re.I):
     func(mail1, mail2, psw)
   
def main():
 mail_to =  raw_input("Enter the account to send notification from : ")
 mail_from = raw_input("Enter the account to send notification to: ")
 password = raw_input("Enter the password for sending the notification: ")
 logs_notification(send, mail_to, mail_from, password)
 print "Notification is sent"
if __name__ == "__main__":
 main()
