import argparse
import subprocess
import fileinput
from jinja2 import Environment, FileSystemLoader
import sys
import os

def main():
 j2_env = Environment(loader=FileSystemLoader('/kubernetes/templates'), trim_blocks=True)
 parser = argparse.ArgumentParser(description='MavenCode Kubernetes cluster Deployment')
 '''
   Add Arguments
 '''
 parser.add_argument('--name', type=str, help='Cluster name', required=True)
 parser.add_argument('--additional_zones', type=str, help='The set of additional zones in which the specified node footprint should be replicated. All zones must be in the same region as the cluster primary zone', required=False)
 parser.add_argument('--async', action='store_true', help='Display informations about the operation in progress, without waiting for the operation to complete', required=False)
 parser.add_argument('--addons', type=str, help='Default set of addons includes HttpLoadBalancing, HorizontalPodAutoscaling', required=False)
 parser.add_argument('--cluster_ipv4_cidr', type=str, help='The IP address range for the pods in this cluster in CIDR notation (e.g. 10.0.0.0/14)', required=False)
 parser.add_argument('--cluster_secondary_range_name', type=str, help='Set the secondary range to be used as the source for pod IPs', required=False)
 parser.add_argument('--cluster_version', type=str, help='The Kubernetes version to use for the master and nodes', required=False)
 parser.add_argument('--create_subnetwork', type=str, help='Create a new subnetwork for the cluster', required=False)
 
 parser.add_argument('--disk_size', type=str, help='Size in GB for node VM boot disks. Defaults to 100GB', required=False)
 parser.add_argument('--enable_autorepair', action='store_true', help='Sets autorepair feature for a cluster default node-pool(s)', required=False) 
 parser.add_argument('--enable_autoupgrade', action='store_true', help='Sets autoupgrade feature for a cluster default node-pool(s)', required=False)
 parser.add_argument('--enable_cloud_logging', action='store_true', help='Automatically send logs from the cluster to the Google Cloud Logging API. Enabled by default', required=False)
 parser.add_argument('--enable_cloud_monitoring', action='store_true', help='Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API.Enabled by default', required=False)
 parser.add_argument('--enable_ip_alias', action='store_true', help='Enable use of alias IPs for pod IPs', required=False)
 parser.add_argument('--enable_kubernetes_alpha', action='store_true', help='Enable Kubernetes alpha features on this cluster', required=False)
 parser.add_argument('--enable_legacy_authorization', action='store_true', help='Enables the legacy ABAC authentication for the cluster.', required=False)
 parser.add_argument('--enable_network_policy', action='store_true', help='Enable network policy enforcement for this cluster.', required=False)
 parser.add_argument('--image_type', type=str, help='The image type to use for the cluster. Defaults to server-specified.', required=False)
 parser.add_argument('--issue_client_certificate', action='store_true', help='enable the TLS client certificate', required=False)
 parser.add_argument('--no_issue_client_certificate', action='store_true', help='disable the TLS client certificate', required=False)
 parser.add_argument('--labels', type=str, help='Labels to apply to the Google Cloud resources in use by the Kubernetes Engine cluster', required=False)
 parser.add_argument('--scopes', type=str, help='Specifies scopes for the node instances,default="gke-default"', required=False)
 parser.add_argument('--no_enable_cloud_endpoints', action='store_true', help='Remove service-control and service-management scopes, even if they are implicitly (via default) or explicitly set via --scopes.', required=False)
 parser.add_argument('--service_account', type=str, help='The Google Cloud Platform Service Account to be used by the node VMs.If no Service Account is specified, the project default service account is used.', required=False)
 parser.add_argument('--zone', type=str, help='Compute zone (e.g. us-central1-a) for the cluster. Overrides the default compute/zone property value for this command invocation.', required=False)
 parser.add_argument('--region', type=str, help='Compute region (e.g. us-central1) for the cluster.', required=False)
 parser.add_argument('--password', type=str, help='The password to use for cluster auth. Defaults to a server-specified randomly-generated string.', required=False)
 parser.add_argument('--enable_basic_auth', action='store_true', help='Enable basic (username/password) auth for the cluster, a way for specifying a username', required=False)
 parser.add_argument('--username', type=str, help='The user name to use for basic auth for the cluster', required=False)
 parser.add_argument('--master_authorized_networks', type=str, help='The list of CIDR blocks (up to 20) that are allowed to connect to Kubernetes master through HTTPS.', required=False)
 parser.add_argument('--enable_master_authorized_networks', action='store_true', help='Allow only specified set of CIDR blocks (specified by the --master-authorized-networks flag) to connect to Kubernetes master through HTTPS.', required=False)
 parser.add_argument('--max_nodes', type=str, help='Maximum number of nodes in the node pool.Maximum number of nodes to which the node pool specified by --node-pool (or default node pool if unspecified) can scale', required=False)
 parser.add_argument('--min_nodes', type=str, help='Minimum number of nodes in the node pool.Minimum number of nodes to which the node pool specified by --node-pool (or default node pool if unspecified) can scale.', required=False)
 parser.add_argument('--enable_autoscaling', action='store_true', help='Enables autoscaling for a node pool.Enables autoscaling in the node pool specified by --node-pool or the default node pool if --node-pool is not provided.', required=False)
 parser.add_argument('--tags', type=str, help='Cluster tags', required=False)
 parser.add_argument('--subnetwork', type=str, help='The Google Compute Engine subnetwork.The subnetwork must belong to the network specified by --network.', required=False)
 parser.add_argument('--local_ssd_count', type=str, help='The number of local SSD disks to provision on each node.Local SSDs have a fixed 375 GB capacity per device', required=False)
 parser.add_argument('--machine_type', type=str, help='The type of machine to use for nodes. Defaults to n1-standard-1', required=False)
 parser.add_argument('--maintenance_window', type=str, help='Set a time of day when you prefer maintenance to start on this cluster.', required=False)
 parser.add_argument('--max_nodes_per_pool', type=str, help='The maximum number of nodes to allocate per default initial node pool.Defaults to 1000 nodes.', required=False)
 parser.add_argument('--node_labels', type=str, help='Applies the given kubernetes labels on all nodes in the new node-pool.', required=False)
 parser.add_argument('--node_locations', type=str, help='The set of zones in which the specified node footprint should be replicated. All zones must be in the same region as the cluster master(s). If not specified, all nodes will be in the cluster primary zone (for zonal clusters) or spread across three randomly chosen zones within the cluster region (for regional clusters).', required=False)
 parser.add_argument('--node_taints', type=str, help='Applies the given kubernetes taints on all nodes in default node-pool(s) in new cluster.', required=False)
 parser.add_argument('--node_version', type=str, help='The Kubernetes version to use for nodes. Defaults to server-specified. ', required=False)
 parser.add_argument('--num_nodes', type=str, help='The number of nodes to be created in each of the cluster zones', required=False)
 parser.add_argument('--preemptible', action='store_true', help='Create nodes using preemptible VM instances in the new cluster.', required=False)
 parser.add_argument('--services_ipv4_cid', type=str, help='Set the IP range for the services IPs. .', required=False)
 parser.add_argument('--services_secondary_range_name', type=str, help='Set the secondary range to be used for services (e.g. ClusterIPs). NAME must be the name of an existing secondary range in the cluster subnetwork.', required=False)
 parser.add_argument('--accelerator', action='store_true', help='Attaches accelerators (e.g. GPUs) to all nodes. ', required=False)
 parser.add_argument('--accelerator_type', type=str, help='The type of the accelerators to attach . ', required=False)
 parser.add_argument('--accelerator_count', type=str, help='The number of the accelerators to attach . ', required=False)
 parser.add_argument('--create_subnetwork_name', type=str, help='The name of the subnetwork to create. ', required=False)
 parser.add_argument('--create_subnetwork_range', type=str, help='The range of the subnetwork to create. ', required=False)
 parser.add_argument('--go_live', action='store_true', help='if true it will invoke the ansible playbook responsable for deploying the kubernetes cluster on GCP', required=False)
 parser.add_argument('--project_id', type=str, help='projectid needs to be specificied', required=True)
 parser.add_argument('--pubsub_notification', type=str, help='PubSub Notification needs to be specificied', required=True)
 parser.add_argument('--enable_basic_auth', action='store_true', help='Enable basic (username/password) auth for the cluster', required=False) 
 parser.add_argument('--no_enable_basic_auth', action='store_true', help='--no-enable-basic-auth is an alias for --username=""', required=False) 

 args = parser.parse_args()
 name = args.name
 project_id = args.project_id
 pubsub_notification = args.pubsub_notification
 go_live = args.go_live 
 create_subnetwork = args.create_subnetwork
 enable_cloud_logging = args.enable_cloud_logging
 no_enable_cloud_logging = args.no_enable_cloud_logging
 enable_cloud_monitoring = args.enable_cloud_monitoring
 no_enable_cloud_monitoring = args.no_enable_cloud_monitoring
 enable_ip_alias = args.enable_ip_alias
 enable_legacy_authorization = args.enable_legacy_authorization
 no_enable_legacy_authorization = args.no_enable_legacy_authorization
 issue_client_certificate = args.issue_client_certificate
 no_issue_client_certificate = args.no_issue_client_certificate 
 zone = args.zone
 region = args.region 
 enable_basic_auth = args.enable_basic_auth
 username = args.username 
 subnetwork = args.subnetwork
 services_ipv4_cid = args.services_ipv4_cid
 services_secondary_range_name = args.services_secondary_range_name
 accelerator = args.accelerator
 accelerator_type = args.accelerator_type
 create_subnetwork_range = args.create_subnetwork_range
 no_enable_basic_auth = args.no_enable_basic_auth
 create_subnetwork_name = args.create_subnetwork_name
 master_authorized_networks = args.master_authorized_networks
 enable_master_authorized_networks = args.enable_master_authorized_networks

 if not zone and not region:
   print 'you should specify the region or the zone for the cluster'
 if accelerator and not accelerator_type:
   print 'if you want to attach accelerators to the cluster nodes, you must specify the type of the accelerators using --accelerator-type'
 if create_subnetwork and not create_subnetwork_range and not create_subnetwork_name:
   print 'if you want a new subnetwork for the cluster, you must specify either the the name of the subnetwork using --create-subnetwork-name or its range using create-subnetwork-range or both'
 if enable_cloud_logging and no-enable_cloud_logging:
   print 'you should choice either to enable the cloud logging or not, not both of of them at the same time !'
 if enable_cloud_monitoring and no_enable_cloud_monitoring:
   print 'you should choice either to enable the cloud monitoring or not, not both of them at the same time !'
 if enable_legacy_authorization and no_enable_legacy_authorization:
   print 'you should choice either to enable the legacy-authorization or not, not both of them at the same time !'
 if issue_client_certificate and no_issue_client_certificate:
   print 'you should choice either to enable the client certificate or not, not both of them at the same time !'
 if services_ipv4_cid and not enable_ip_alias:
   print 'the IP range for the services IPs is not specified unless --enable-ip-alias is also specified' 
 if services_secondary_range_name and enable_ip_alias and not create_subnetwork:
   print 'services-secondary-range-name must be used in conjunction with --enable-ip-alias. Cannot be used with --create-subnetwork.'
 if subnetwork and not create_subnetwork:
   print 'subnetwork must be used with the "--create-subnetwork" option'
 if enable_master_authorized_networks and not master_authorized_networks:
   print 'master-authorized-networks can not be specified unless --enable-master-authorized-networks is also specified. '
 if enable_basic_auth and not username:
   print 'you should choose specify the username using --username or --enable-basic-auth'
 if enable_basic_auth and no_enable_basic_auth:
   print 'you should choose between --enable-basic-auth or --no-enable-basic-auth'
  
 d = {}
 for arg in vars(args):
  if getattr(args, arg) <> None:
    d.update({arg : getattr(args, arg)})
 d.update({'item':"{{ item }}"})
 template = j2_env.get_template('kubernetes_template.j2')
 task_tmpl = template.render(d=d)
 tasks = task_tmpl % (name, name, name)
 task_file = open('/kubernetes/roles/kubernetes/tasks/main.yml', 'w')
 task_file.write(tasks)
 task_file.close()
 for line in fileinput.FileInput("/kubernetes/roles/kubernetes/tasks/main.yml",inplace=1):
  line = line.rstrip()
  if line != '':
    print line

 '''
 Generate Job Run Setup Yaml
 '''

 setup_tmpl = """
 - hosts: localhost
   connection: local
   roles:
    - role: kubernetes
      project_id: '%s'
      pubsub_topic_url: '%s'    
 """
 setup_info = setup_tmpl % (project_id, pubsub_notification)
 playbook_filename = "setup_%s.yml" % project_id
 playbook_file = open(playbook_filename, 'w')
 playbook_file.write(setup_info)
 playbook_file.close()

 if go_live:
  deploy_cmd = "ansible-playbook /kubernetes/%s -i /kubernetes/inventory.ini" % playbook_filename
  subprocess.call([deploy_cmd], shell=True)

if __name__ == "__main__":
 main()     
