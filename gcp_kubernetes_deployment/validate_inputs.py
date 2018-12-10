import re
import subprocess
import os

def validate_name(arg):
 m = re.match("^[a-z].[a-z-0-9]+$", arg)
 print bool(m)

def validate_number(arg):
 m = re.match("^[1-9][0-9]+$", arg)
 print bool(m)

def validate_image_type(arg):
 if arg in ['UBUNTU','COS']:
  print 'ok'

def validate_zone(arg):
 proc = subprocess.Popen(["gcloud compute zones list | awk '{print $1}' | awk '{ if ( NR > 1  ) { print } }'"], stdout=subprocess.PIPE, shell=True)
 output = proc.stdout.readlines()
 zones = []
 for line in output:
  zones.append(line.strip())
 if arg in zones:
  print 'ok'
  return True

def validate_region(arg):
 proc = subprocess.Popen(["gcloud compute regions list | awk '{print $1}' | awk '{ if ( NR > 1  ) { print } }'"], stdout=subprocess.PIPE, shell=True)
 output = proc.stdout.readlines() 
 regions = []
 for line in output:
  regions.append(line.strip())
 if arg in regions:
  print 'ok'

def validate_machine_type(arg, zone):
 proc = subprocess.Popen(["gcloud compute machine-types list | grep "+ zone +" | awk '{print $1}' | awk '{ if ( NR > 1  ) { print } }'"], stdout=subprocess.PIPE, shell=True)
 output = proc.stdout.readlines()
 machine_types = []
 for line in output:
  machine_types.append(line.strip())
 if arg in machine_types:
  print 'ok' 

def validate_key_value(arg):
 m = re.match("^[a-z].[,=a-z-0-9]+$", arg)
 print bool(m)
 
def disk_type(arg):
 disk_types = ['pd-standard','pd-ssd']
 if arg in disk_types:
  print 'ok'  
   
def disk_size(arg):
 m = re.match("^[1-9].[0-9]+GB$", arg)
 print bool(m)

def validate_node_locations(arg,zone):
 m = re.match("^[a-z].[,a-z-0-9]+$", arg)
 node_locations = arg.split(',')
 if zone in node_locations and bool(m):
   print 'ok'

def validate_node_version(arg,zone, master_version):
 proc = subprocess.Popen(["gcloud container get-server-config --zone "+zone+" | awk '{ if ( NR > 6  ) { print } }'"], stdout=subprocess.PIPE, shell=True)
 output = proc.stdout.readlines()
 node_versions = []
 for i in output:
  i = i.rstrip()
  node_versions.append(i.lstrip('- '))
 if arg in node_versions[node_versions.index('validNodeVersions:'):][1:] and int(master_version.split('.')[1]) - int(arg.split('.')[1]) <= 2:
  print 'ok'
 
def validate_tags(arg, zone):
 m = re.match("^[a-z].[,a-z-0-9]+$", arg)
 if bool(m):
  print 'ok'

def validate_accelerator(arg, zone): 
 proc = subprocess.Popen(["gcloud compute accelerator-types list --filter='zone:( "+zone+" )' | awk '{print $1}' | awk '{ if ( NR > 1  ) { print } }'"], stdout=subprocess.PIPE, shell=True)
 output = proc.stdout.readlines()
 accelerators = []
 for i in output:
  i = i.strip()
  accelerators.append(i)
 m = re.match("^type=.[,=a-z-0-9]+[1-9]+$", arg)
 if bool(m):
  if arg.split(',')[0].startswith('type=') and arg.split(',')[1].startswith('count='): 
  
    if arg.split(',')[0].split('=')[1] in accelerators :
      print 'ok'

def validate_additional_zones(arg):
 m = re.match("^[,a-z-0-9]+$", arg)
 for zone in arg.split(','):
  if validate_zone(zone) and bool(m):
   print 'ok'

def validate_addons(arg):
 addons = ['HttpLoadBalancing','HorizontalPodAutoscaling','KubernetesDashboard','Istio','NetworkPolicy']
 if arg in addonns:
  print 'ok'

def validate_cluster_ipv4_cidr(arg):
 m = re.match("^$|([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])((/([01]?\\d\\d?|2[0-4]\\d|25[0-5]))?)$", arg)
 if bool(m):
  print 'ok'

def validate_cluster_version(arg, zone):
 proc= subprocess.Popen(["gcloud container get-server-config --zone "+zone+" | awk '{ if ( NR > 6  ) { print } }'"], stdout=subprocess.PIPE, shell=True)
 output = proc.stdout.readlines()
 master_versions = []
 node_versions = []
 for i in output:
  i = i.rstrip()
  master_versions.append(i.lstrip('- '))
 node_versions = master_versions[master_versions.index('validNodeVersions:'):][1:]
 master_versions = master_versions[:master_versions.index('validNodeVersions:')]
 cluster_versions = list(set(node_versions) & set(master_versions))
 if arg in cluster_versions:
  print 'ok'

def validate_create_subnetwork(arg):
 
if __name__ == "__main__":
  validate_node_version('1.8.8-gke.0','us-central1-c','1.10.6-gke.1')
