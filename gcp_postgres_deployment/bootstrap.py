import argparse
import subprocess
from jinja2 import Environment, FileSystemLoader
import fileinput
def main():
 parser = argparse.ArgumentParser(description='Boostrap a Google Cloud Postgres instance using Cloud Sql')
 '''
  Add Arguments
 '''
 parser.add_argument('--instance_name', type=str, help='the name of the postgres instance', required=True)
 parser.add_argument('--database_version', type=str, help='the database version', required=False)
 parser.add_argument('--activation_policy', type=str, help='the activation policy for this instance', required=False)
 parser.add_argument('--assign_ip', action='store_true', help='assign an IP address', required=False)
 parser.add_argument('--async', action='store_true', help='display information about the operation in progress', required=False)
 parser.add_argument('--authorized_gae_apps', type=str, help='list of project IDs for App Engine applications running in the Standard environment that can access this instance', required=False)
 parser.add_argument('--authorized_networks', type=str, help='the list of external networks that are allowed to connect to the instance', required=False)
 parser.add_argument('--availability_type', type=str, help='Specifies level of availability: it can be zonal or regional', required=False) 
 parser.add_argument('--backup', action='store_true', help='enables daily backup', required=False)
 parser.add_argument('--backup_start_time', type=str, help='the start time of daily backups', required=False)
 parser.add_argument('--cpu', type=str, help='how many cores are desired in the machine', required=False)
 parser.add_argument('--database_flags', type=str, help='a comma-separated list of database flags to set on the instance', required=False)
 parser.add_argument('--enable_bin_log', action='store_true', help='Specified if binary log should be enabled', required=False)
 parser.add_argument('--failover_replica_name', type=str, help='create a failover replica with the specified name', required=False)
 parser.add_argument('--follow_gae_app', type=str, help='the App Engine app this instance should follow', required=False)
 parser.add_argument('--gce_zone', type=str, help='the preferred Compute Engine zone', required=False)
 parser.add_argument('--maintenance_release_channel', type=str, help='Which channel updates to apply during the maintenance window must be preview or production', required=False)
 parser.add_argument('--maintenance_window_day', type=str, help='Day of week for maintenance window, in UTC time zone must be SUN,MON,TUE,WED,THU,FRI,SAT', required=False)
 parser.add_argument('--maintenance_window_hour', type=str, help='Hour of day for maintenance window, in UTC time zone', required=False)
 parser.add_argument('--master_instance_name', type=str, help='name of the instance which will act as master in the replication setup', required=False)
 parser.add_argument('--memory', type=str, help='a whole number value indicating how much memory is desired in the machine', required=False)
 parser.add_argument('--pricing_plan', type=str, help='the pricing plan for this instance.', required=False)
 parser.add_argument('--region', type=str, help='the regional location', required=False)
 parser.add_argument('--replica_type', type=str, help='the type of replica to create must be READ or FAILOVER', required=False)
 parser.add_argument('--replication', type=str, help='the type of replication this instance uses must be synchronous or asynchronous', required=False)
 parser.add_argument('--require_ssl', action='store_true', help='specified if users connecting over IP must use SS', required=False)
 parser.add_argument('--storage_auto_increase', action='store_true', help='storage size can be increased', required=False)
 parser.add_argument('--storage_size', type=str, help='amount of storage allocated to the instance', required=False)
 parser.add_argument('--storage_type', type=str, help='the storage type for the instance. The default is SSD', required=False)
 parser.add_argument('--tier', type=str, help='the tier for this instance', required=False)
 parser.add_argument('--go_live', action='store_true', help='deploy the postgres instance', required=False) 
 args = parser.parse_args()
 go_live = args.go_live
 d = {}
 for arg in vars(args):
  if getattr(args, arg) <> None:
   d.update({arg : getattr(args, arg)})
 j2_env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)
 template = j2_env.get_template('postgres_template.j2')
 task_tmpl = template.render(d=d)
 task_file = open('roles/postgres/tasks/main.yml', 'w')
 task_file.write(task_tmpl)
 task_file.close()
 for line in fileinput.FileInput("roles/postgres/tasks/main.yml",inplace=1):
  line = line.rstrip()
  if line != '':
   print line
 if go_live:
  deploy_cmd = "ansible-playbook roles/postgres/tasks/main.yml -i inventory.ini"
  subprocess.call([deploy_cmd], shell=True)
if __name__ == "__main__":
 main()
