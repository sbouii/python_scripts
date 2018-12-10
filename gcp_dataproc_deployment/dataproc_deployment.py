#-*- coding: utf-8 -*-
import argparse
import fileinput
import subprocess
from jinja2 import Environment, FileSystemLoader
import sys

def main():
 j2_env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)
 parser = argparse.ArgumentParser(description='MavenCode Dataproc cluster Deployment')
 ''' 
   Add Arguments
 '''
 parser.add_argument('--name', type=str, help='Cluster name', required=True)
 parser.add_argument('--zone', type=str, help='The zone where the cluster will be deployed', required=False)
 parser.add_argument('--region', type=str, help='The region where cluster will be deployed', required=False)
 parser.add_argument('--image', type=str, help='The full custom image URI or the custom image name that will be used to create a cluster', required=False)
 parser.add_argument('--image_version', type=str, help='The image version to use for the cluster', required=False)
 parser.add_argument('--bucket', type=str, help='The Google Cloud Storage bucket to use with the Google Cloud Storage connector.A bucket is auto created when this parameter is not specified', required=False)

 parser.add_argument('--labels', type=str, help='A list of label KEY=VALUE pairs to add. Keys and values must start with a lowercase character and contain only hyphens (-), underscores (_), lowercase characters, and numbers.', required=False)
 parser.add_argument('--metadata', type=str, help='A list of Metadata KEY=VALUE pairs to be made available to the guest operating system running on the instances', required=False)
 parser.add_argument('--properties', type=str, help='The configuration properties for installed packages, such as Hadoop and Spark. --properties=[PREFIX:PROPERTY=VALUE,…]', required=False)
 parser.add_argument('--tags', type=str, help='A list of tags to apply to the instances for identifying the instances to which network firewall rules will apply. --tags=TAG,[TAG,…]', required=False)

 parser.add_argument('--master_machine_type', type=str, help='Master machine type. Defaults to server-specified', required=False)
 parser.add_argument('--master_boot_disk_size', type=str, help='The size of the boot disk.The value must be a whole number followed by a size unit of KB,MB,GB,TB.For example 20GB.Minimum size is 10 GB', required=False)
 parser.add_argument('--master_boot_disk_type', type=str, help='The type of the boot disk. The value must be pd-standard or pd-ssd', required=False)
 parser.add_argument('--num_master_local_ssds', type=str, help='The number of local SSDs to attach to the master in a cluster', required=False)
 parser.add_argument('--masters_number', type=str, help='Number of masters in the cluster', required=False)

 parser.add_argument('--worker_machine_type', type=str, help='Worker machine type. Defaults to server-specified', required=False)
 parser.add_argument('--worker_boot_disk_size', type=str, help='The size of the boot disk.The value must be a whole number followed by a size unit of KB,MB,GB,TB.For example 10GB', required=False)
 parser.add_argument('--worker_boot_disk_type', type=str, help='The type of the boot disk. The value must be pd-standard or pd-ssd', required=False)
 parser.add_argument('--num_worker_local_ssds', type=str, help='The number of local SSDs to attach to each worker in a cluster', required=False)
 parser.add_argument('--num_preemptible_workers', type=str, help='The number of preemptible worker nodes in the cluster', required=False)
 parser.add_argument('--preemptible_worker_boot_disk_size', type=str, help='The size of the boot disk. The value must be a whole number followed by a size unit of KB,MB,GB,TB', required=False)
 parser.add_argument('--preemptible_worker_boot_disk_type', type=str, help='The type of the boot disk. The value must be pd-standard or pd-ssd', required=False) 
 parser.add_argument('--workers_number', type=str, help='Number of workers in the cluster', required=False)

 parser.add_argument('--initialization_actions', type=str, help='A list of Google Cloud Storage URIs of executables to run on each node in the cluster.--initialization-actions=CLOUD_STORAGE_URI,[…]', required=False)
 parser.add_argument('--initialization_actions_timeout', type=str, help='The maximum duration of each initialization action', required=False)
 
 parser.add_argument('--network', type=str, help='The Compute Engine network that the VM instances of the cluster will be part of', required=False)
 parser.add_argument('--subnet', type=str, help='The subnet that the cluster will be part of. This is mutally exclusive with --network', required=False)
 parser.add_argument('--single_node', action='store_true', help='Create a single node cluster that has all master and worker components. ', required=False)
 parser.add_argument('--scopes', type=str, help='The scopes for the node instances. Multiple SCOPEs can be specified, separated by commas.--scopes=SCOPE,[SCOPE,…]', required=False)
 parser.add_argument('--async', action='store_true', help='display informations about the operation in progress, without waiting for the operation to complete', required=False)
 parser.add_argument('--job_language', type=str, help='the language of the job , it can be jar or python', required=True)
 parser.add_argument('--job_python', type=str, help='the bucket url where the python job script exists', required=False)
 parser.add_argument('--job_jar', type=str, help='the bucket url where jar file job exists', required=False)
 parser.add_argument('--job_class', type=str, help='the class containing the main method, must be in a provided jar or jar that is already on the classpath.', required=False)
 parser.add_argument('--job_py_files', type=str, help='comma separated list of bucket urls where python files that will be provided to the job exists', required=False)
 parser.add_argument('--job_files', type=str, help='comma separated list of bucket urls where the job files exist', required=False)
 parser.add_argument('--job_archives', type=str, help='comma separated list of bucket urls where archives that will be provided to the job exists', required=False)
 parser.add_argument('--job_async', type=str, help='display informations about the job submitting in progress', required=False)
 parser.add_argument('--job_bucket', type=str, help='the Cloud Storage bucket to stage files in. Defaults to the cluster configured bucket', required=False)
 parser.add_argument('--job_driver_log_levels', type=str, help='list of key value pairs to configure driver logging, where key is a package and value is the log4j log level. --driver-log-levels=[PACKAGE=LEVEL,…]] ', required=False)
 parser.add_argument('--job_jars', type=str, help='comma separated list of bucket urls where the jar files to be provided to the executor exists', required=False)
 parser.add_argument('--job_labels', type=str, help='a list of label KEY=VALUE pairs to add', required=False)
 parser.add_argument('--job_properties', type=str, help='a list of key value pairs to configure PySpark. --properties=[PROPERTY=VALUE,…]]', required=False)
 parser.add_argument('--job_max_failures_per_hour', type=str, help='specifies maximum number of times a job can be restarted in event of failure', required=False)
 parser.add_argument('--job_arguments', type=str, help='arguments to pass to the python job', required=False)
 parser.add_argument('--storage_bucket', type=str, help='a bucket where the job related files are stored', required=False)
 parser.add_argument('--go_live', action='store_true', help='if true it will invoke the ansible playbook responsable for deploying the dataproc cluster on GCP', required=False)

 args = parser.parse_args()
 job_language = args.job_language
 storage_bucket = args.storage_bucket
 job_language = args.job_language
 job_jar = args.job_jar
 job_class = args.job_class
 job_python = args.job_python
 zone = args.zone
 region = args.region
 job_py_files = args.job_py_files
 job_files = args. job_files
 job_archives = args.job_archives
 job_jars = args.job_jars
 job_file_location = args.job_file_location
 name = args.name
 go_live = args.go_live

 if job_language and not storage_bucket:
   print 'if you want to submit a job, you must provide the bucket where the job related files exist using --storage_bucket' 
 if job_language == 'jar' and not job_jar and not job_class:
   print 'if the job is a jar job, it requires the --job_jar argument or the --job_class argument'
   sys.exit(-1)
 if job_language == 'python' and not job_python:
   print 'if the job is a python job, it requires the --job_python argument'
   sys.exit(-1)
 if not zone and not region:
   print 'you should specify either the --zone or the --region argument'
   sys.exit(-1)
 if job_python:
  download_command = "gsutil cp %s/%s /dataproc/roles/dataproc/files/" % (storage_bucket, job_python)
  subprocess.call([download_command], shell=True)
 if job_jar:
  download_command = "gsutil cp %s/%s /dataproc/roles/dataproc/files/" % (storage_bucket, job_jar)
  subprocess.call([download_command], shell=True)
 if job_py_files:
  download_command = "gsutil cp %s/%s /dataproc/roles/dataproc/files/" % (storage_bucket, job_py_files)
  subprocess.call([download_command], shell=True)
 if job_files:
  download_command = "gsutil cp %s/%s /dataproc/roles/dataproc/files/" % (storage_bucket, job_files)
  subprocess.call([download_command], shell=True)
 if job_archives:
  download_command = "gsutil cp %s/%s /dataproc/roles/dataproc/files/" % (storage_bucket, job_archives)
  subprocess.call([download_command], shell=True)
 if job_jars:
  download_command = "gsutil cp %s/%s /dataproc/roles/dataproc/files/" % (storage_bucket, job_jars)
  subprocess.call([download_command], shell=True)

 d = {} 
 for arg in vars(args):  
  if getattr(args, arg) <> None:
   d.update({arg : getattr(args, arg)})  	
 template = j2_env.get_template('dataproc_template.j2')
 task_tmpl = template.render(d=d)
 if job_language == 'python':
  job_file_location = '/dataproc/roles/dataproc/files/'+ job_python 
  tasks = task_tmpl % (name, name, job_file_location, name, name) 
 if job_language == 'jar':
  tasks = task_tmpl % (name, name, name)
 task_file = open('/dataproc/roles/dataproc/tasks/main.yml', 'w')
 task_file.write(tasks)
 task_file.close()
 for line in fileinput.FileInput("/dataproc/roles/dataproc/tasks/main.yml",inplace=1):
   line = line.rstrip()
   if line != '':
    print line
 if go_live: 
  subprocess.call(["ansible-playbook /dataproc/setup.yml -i /dataproc/inventory.ini"], shell=True)
if __name__ == "__main__":
 main()
