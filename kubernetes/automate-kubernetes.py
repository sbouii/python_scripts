import subprocess
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

def run_pods(func1, func2, mes1, mes3 , mes4, mes5, mes6, mes7, mes8):
   parser = argparse.ArgumentParser(description='This Python script deploys docker conatiners on kubernetes cluster')
   parser.add_argument('-f', '--filedeployment', help='The relatif path of the deployment file')
   parser.add_argument('-d', '--delete', help='the name of the pod to delete enter all if you want to delete all')
   parser.add_argument('-i', '--clusterinfo', help='the informations of your cluster', action='store_true')

   args = parser.parse_args()
   if len(sys.argv) == 1:
     func2(mes1)
     subprocess.call(["sudo", "minikube", "start"])
     func2(mes5)     
     parser.print_help()

   else:
    if args.filedeployment:
     if os.path.isfile(args.filedeployment):    
                
       subprocess.call(["sudo", "kubectl", "create", "-f", args.filedeployment])                      
     else:
       func1(mes3)
       sys.exit(1)

    if args.delete:     
       subprocess.call(["sudo", "kubectl", "delete", "service", args.delete])
       subprocess.call(["sudo", "kubectl", "delete", "deployment", args.delete])
       if args.delete == "all":       
         subprocess.call(["sudo", "kubectl", "delete", "pods","--all"])
         subprocess.call(["sudo", "kubectl", "delete", "services","--all"])
         subprocess.call(["sudo", "kubectl", "delete", "deployments","--all"])
    if args.clusterinfo:
       func2(mes6)
       subprocess.call(["sudo", "kubectl", "cluster-info"])
       func2(mes7)  
       subprocess.call(["sudo", "kubectl", "get", "nodes"])
       func2(mes8)
       subprocess.call(["sudo", "kubectl", "get", "pods"])
       
def main():
   
   message_error3 = "Please check the path of the deployment file \n "
   message_error4 = "Please enter the name of the pod to delete or enter -all to delete all the existing pods \n "
   message_result1 = "Setting up your kubernetes cluster *********************************** \n"
   message_result2 = "Here the different operations that you can make on the cluster \n"
   message_result3 = "Here the general informations of your cluster:"
   message_result4 = "Here the nodes of your cluster:"
   message_result5 = "Here the deployed pods on your cluster:"
   run_pods(display_error, display_result, message_result1, message_error3, message_error4, message_result2, message_result3, message_result4, message_result5)
if __name__ == "__main__":
   main()
