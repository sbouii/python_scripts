import argparse
import subprocess
import fileinput
from jinja2 import Environment, FileSystemLoader
import sys
import os

def main():
 j2_env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)
 parser = argparse.ArgumentParser(description='Boostrap a Google cloud instance using Google deployment manager')
 '''
  Add Arguments
 '''
 parser.add_argument('--instance_name', type=str, help='a name for the Google cloud instance to be deployed', required=True)
 parser.add_argument('--deployment_name', type=str, help='a name for the Google cloud deployment', required=True)
 parser.add_argument('--template', type=str, help='the template of the Google cloud deployment', required=True)
 parser.add_argument('--zone', type=str, help='the zone where the Google cloud instnace will be deployed', required=True)
 parser.add_argument('--machineType', type=str, help='the Google cloud instance type', required=True)
 parser.add_argument('--deviceName', type=str, help='the name of the disk', required=True)
 parser.add_argument('--type', type=str, help='the type of the disk', required=True)
 parser.add_argument('--boot', type=str, help='if the disk is used as boot or not', required=True)
 parser.add_argument('--autoDelete', type=str, help='autodelete the data on the disk or not', required=True)
 parser.add_argument('--imageProject', type=str, help='the project of the os image to use', required=True)
 parser.add_argument('--imageFamily', type=str, help='the Family of the os image to use', required=True)
 parser.add_argument('--networkName', type=str, help='the network name to use for the Google cloud instance', required=True)
 parser.add_argument('--networkType', type=str, help='the network type to use for the Google cloud instance', required=True)
 parser.add_argument('--deploy_jenkins', action='store_true', help='deploy jenkins instance', required=False)
 parser.add_argument('--deploy_postgres', action='store_true', help='deploy postgres instance', required=False)
 parser.add_argument('--go_live', action='store_true', help='invoke the deployment of the instance', required=False)
 args = parser.parse_args() 
 go_live = args.go_live
 d = {}
 for arg in vars(args):
  d.update({arg : getattr(args, arg)})
 d.update({'item':"{{ item }}"})
 d.update({'retries':"{{ retries }}"})
 d.update({'delay':"{{ delay }}"})
 template = j2_env.get_template('main.j2')
 task_tmpl = template.render(d=d)
 if deploy_jenkins:
  task_file = open('roles/jenkins/tasks/main.yml', 'w')
 if deploy_postgres:
  task_file = open('roles/postgres/tasks/main.yml', 'w')
 task_file.write(task_tmpl)
 task_file.close() 
 for line in fileinput.FileInput("roles/jenkins/tasks/main.yml",inplace=1):
  line = line.rstrip()
  if line != '':
    print line
 if go_live and deploy_jenkins:
  deploy_cmd = "ansible-playbook jenkins.yml -i inventory.ini"
  subprocess.call([deploy_cmd], shell=True)
 if go_live and deploy_postgres:
  deploy_cmd = "ansible-playbook postgres.yml -i inventory.ini"
  subprocess.call([deploy_cmd], shell=True)
if __name__ == "__main__":
 main()

