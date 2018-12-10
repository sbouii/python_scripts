import subprocess
from subprocess import check_output
import sys
import os

FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'
FNULL = open(os.devnull, 'w')

def display_message(message):
   print OKGREEN + BOLD + UNDERLINE + message + ENDC

def kubernetes_service_account(func, project_id):
   func('Creating kubernetes service account ...')
   enable_kubernets_cmd = "gcloud services enable container.googleapis.com"
   subprocess.call([enable_kubernets_cmd], stdout=FNULL, shell=True)
   check_service_account = "gcloud iam service-accounts list | grep sa-kubernetes"
   service_accounts = subprocess.Popen([check_service_account], stdout=subprocess.PIPE, shell=True)
   if service_accounts != "":
    kubernetes_service_account = "sa-kubernetes@%s.iam.gserviceaccount.com" % project_id
    subprocess.call(["sudo gcloud iam service-accounts delete "+ kubernetes_service_account + " --quiet"], stdout=FNULL, shell=True)
    kubernetes_cmd = "gcloud iam service-accounts create sa-kubernetes --display-name " + '"%s kubernetes service account"' % project_id
    subprocess.call([kubernetes_cmd], stdout=FNULL, shell=True)
    print 'Here the email of kubernetes service account ' + kubernetes_service_account
    func('Granting the required roles to the kubernetes service account ... ')
    kubernetes_json_cmd = "gcloud projects add-iam-policy-binding %s --member serviceAccount:%s  --role roles/container.admin" % ( project_id, kubernetes_service_account )
    subprocess.call([kubernetes_json_cmd], stdout=FNULL, shell=True)
    func('Generating the keys of kubernetes service account ...')
    kubernetes_generate_cmd = "gcloud iam service-accounts keys create keys/sa-%s-kubernetes.json --iam-account %s" % ( project_id, kubernetes_service_account )
    subprocess.call([kubernetes_generate_cmd], stdout=FNULL, shell=True)
    print 'kubernetes service account keys created keys/sa-%s-kubernetes.json' % project_id

def dataproc_service_account(func, project_id):
   func('Creating dataproc service account ...')
   enable_dataproc_cmd = "gcloud services enable dataproc.googleapis.com"
   subprocess.call([enable_dataproc_cmd], stdout=FNULL, shell=True)
   check_service_account = "gcloud iam service-accounts list | grep sa-dataproc"
   service_accounts = subprocess.Popen([check_service_account], stdout=subprocess.PIPE, shell=True)
   if service_accounts != "":
    dataproc_service_account = "sa-dataproc@%s.iam.gserviceaccount.com" % project_id
    subprocess.call(["gcloud iam service-accounts delete "+ dataproc_service_account + " --quiet"], stdout=FNULL, shell=True)
    dataproc_cmd = "gcloud iam service-accounts create sa-dataproc --display-name " + '"%s dataproc service account"' % project_id
    subprocess.call([dataproc_cmd], stdout=FNULL, shell=True)
    print 'Here the email of dataproc service account' + dataproc_service_account
    func('Cranting the required roles to dataproc service account ...')
    dataproc_json_cmd = "gcloud projects add-iam-policy-binding %s --member serviceAccount:%s  --role roles/editor" % ( project_id, dataproc_service_account )
    subprocess.call([dataproc_json_cmd], stdout=FNULL, shell=True)
    func('Generating the keys of dataproc service account ...')
    dataproc_generate_cmd = "gcloud iam service-accounts keys create keys/sa-%s-dataproc.json --iam-account %s" % ( project_id, dataproc_service_account )
    subprocess.call([dataproc_generate_cmd], stdout=FNULL, shell=True)
    print 'dataproc service account keys created at keys/sa-%s-dataproc.json' % project_id

def pubsub_service_account(func, project_id):
   func('Creating pubsub service account ...')
   enable_pubsub_cmd = "gcloud services enable pubsub.googleapis.com"
   subprocess.call([enable_pubsub_cmd], stdout=FNULL, shell=True)
   check_service_account = "gcloud iam service-accounts list | grep sa-pubsub"
   service_accounts = subprocess.Popen([check_service_account], stdout=subprocess.PIPE, shell=True)
   if service_accounts != "":
    pubsub_service_account = "sa-pubsub@%s.iam.gserviceaccount.com" % project_id
    subprocess.call(["gcloud iam service-accounts delete "+ pubsub_service_account + " --quiet"], stdout=FNULL, shell=True)
    pubsub_cmd = "gcloud iam service-accounts create sa-pubsub --display-name "+ '"%s pubsub service account"' % project_id
    subprocess.call([pubsub_cmd], stdout=FNULL, shell=True)
    print 'Here the email of pubsub service account' + pubsub_service_account
    func('Granting the required roles to pubsub service account ...')
    pubsub_json_cmd = "gcloud projects add-iam-policy-binding %s --member serviceAccount:%s --role roles/pubsub.editor" % ( project_id, pubsub_service_account )
    subprocess.call([pubsub_json_cmd], stdout=FNULL, shell=True)
    func('Generating the keys of pubsub service account ...')
    pubsub_generate_cmd = "gcloud iam service-accounts keys create keys/sa-%s-pubsub.json --iam-account %s" % ( project_id, pubsub_service_account )
    subprocess.call([pubsub_generate_cmd], stdout=FNULL, shell=True)
    print 'pubsub service account keys created at keys/sa-%s-pubsub.json' % project_id

def add_service_account(kubernetes_func, dataproc_func, pubsub_func, func, project_id):
   print 'If you have already created the kubernetes or the dataproc service account you need to create the pubsub service account !'
   print 'Choose the service account to add: \n 0- Kubernetes service account \n 1- Dataproc service account \n 2- Pubsub service account \n 3- Add no service account'
   add_service_account_choice = int(raw_input("Please enter your numeric choice:"))
   if add_service_account_choice == 0:
     kubernetes_func(func, project_id)
   if add_service_account_choice == 1:
     dataproc_func(func, project_id) 
   if add_service_account_choice == 2:
     pubsub_func(func, project_id)
   if add_service_account_choice == 3:
     sys.exit(0)
   add_service_account(kubernetes_func, dataproc_func, pubsub_func, func, project_id)
def provision(kubernetes_func, dataproc_func, pubsub_func, add_service_func, func):
 '''
  Download gcloud if it does not exist
 ''' 
 check_gcloud = check_output("gcloud version | grep gsutil\n", shell=True)
 if "gsutil" not in check_gcloud: 
  subprocess.call(["curl https://sdk.cloud.google.com | bash"], shell=True)  
  subprocess.call(["gcloud init"], shell=True)
 else:
  func("\n gcloud is already installed !")
 '''
  Initiate gcloud
 '''
 print 'Choose from the options below:\n 0- initiate gcloud \n 1- gcloud is already initiated'
 initiate_choice = int(raw_input("Please enter your numeric choice :"))
 if initiate_choice == 0:
  subprocess.call(["gcloud init"], shell=True) 
 if initiate_choice == 1:
  print 'Use existing account or create new account :\n 0- Use existing account \n 1- Log in with a new account'
  account_choice = int(raw_input("Please enter your numeric choice :"))
  if account_choice ==1:
   subprocess.call(["gcloud init"], shell=True)
  if account_choice ==0:
   proc1 = subprocess.Popen(["gcloud auth list | grep @"], stdout=subprocess.PIPE, shell=True)
   output1 = proc1.stdout.readlines()
   email_account_dict = {}
   i = 0
   for line in output1:
    email_account_dict.update({i:line.strip(' *').strip()})
    i = i+1
   print 'Choose the account you would like to use to perform the operations: '
   for x, y in email_account_dict.items():
    print str(x) +"- "+ y
   email_account_choice = int(raw_input("Please enter your numeric choice :"))
   email_account = email_account_dict.get(email_account_choice)
   subprocess.call(["gcloud config set account " + str(email_account)], shell=True)
   print 'Use existing project or create new project :\n 0- Use existing project \n 1- Create a new project'
   project_choice = int(raw_input("Please enter your numeric choice :"))
   if account_choice ==1:
    project_id = int(raw_input("Please enter a project id example airy-office-125814:"))
    subprocess.call(["gcloud projects create "+ project_id], shell=True)
    subprocess.call(["gcloud config set project "+ project_id], shell=True)
   if account_choice ==0:
    proc2 = subprocess.Popen(["gcloud projects list | awk '{print $1}' | awk '{ if ( NR > 1  ) { print } }'"], stdout=subprocess.PIPE, shell=True)
    output2 = proc2.stdout.readlines()
    project_id_dict = {}
    i = 0
    for line in output2:
     project_id_dict.update({i:line.strip()})
     i = i+1
    print 'Choose the project you would like to use to perform the operations: '
    for x, y in project_id_dict.items():
     print str(x) +"- "+ y
    project_choice = int(raw_input("Please enter your numeric choice :"))
    project_id = project_id_dict.get(project_choice)
    subprocess.call(["gcloud config set project " + str(project_id)], shell=True)
 '''
  Check if the project is already linked to a billing account 
 '''
 print 'linking your selected project to a billing account :'
 proc3 = subprocess.Popen(["gcloud alpha billing projects describe " + project_id], stdout=subprocess.PIPE, shell=True)
 output3 = proc3.stdout.read()
 if 'true' in output3:
  print 'your project is already linked to a billing account !'
 else:
  proc4 = subprocess.Popen(["gcloud alpha billing accounts list | awk '{print $1}' | awk '{ if ( NR > 1  ) { print } }'"], stdout=subprocess.PIPE, shell=True)
  output4 = proc3.stdout.readlines()
  billing_account_dict = {}
  i = 0
  for line in output3:
   billing_account_dict.update({i:line.strip()})
   i = i+1
  if len(billing_account_dict) != 0: 
   print 'Choose the billing account you would like to use to perform the operations: '
  for x, y in billing_account_dict.items():
   print str(x) +"- "+ y
   billing_account_choice = int(raw_input("Please enter your numeric choice :"))
   billing_account_id = billing_account_dict.get(billing_account_choice)
   subprocess.call(["gcloud alpha billing projects link "+ project_id +" --billing-account " + billing_account_id], shell=True)
 
 '''
  Create the service accounts  
 '''
 print 'Choose the service account to create: \n 0- Kubernetes service account \n 1- Dataproc service account \n 2- Pubsub service account \n 3- Create no service account'
 service_account_choice = int(raw_input("Please enter your numeric choice:"))
 if service_account_choice == 0:
   kubernetes_func(func, project_id)
   add_service_func(kubernetes_func, dataproc_func,  pubsub_func, func, project_id)   
 if service_account_choice == 1:
   dataproc_func(func, project_id)
   add_service_func(kubernetes_func, dataproc_func,  pubsub_func, func, project_id)
 if service_account_choice == 2:
   pubsub_func(func, project_id)
   add_service_func(kubernetes_func, dataproc_func,  pubsub_func, func, project_id)
 if service_account_choice == 3:
   sys.exit()
def main():
 provision(kubernetes_service_account, dataproc_service_account, pubsub_service_account, add_service_account, display_message)
if __name__ == "__main__":
 main()
