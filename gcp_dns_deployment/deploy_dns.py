import argparse
import subprocess

def main():
 parser = argparse.ArgumentParser(description='Create a managed zone on Google cloud platform')
 '''
  Add arguments
 '''
 parser.add_argument('--zone_name', type=str, help='the name of the zone to create', required=True)
 parser.add_argument('--dns_suffix', type=str, help='the DNS name suffix that will be managed with the created zone', required=True)
 parser.add_argument('--description', type=str, help='short description for the managed-zone', required=True)
 parser.add_argument('--ip_address', type=str, help='the ip address for the A record', required=True)
 parser.add_argument('--tll', type=str, help='the tll for the A record', required=True) 

 args = parser.parse_args()
 zone_name = args.zone_name
 dns_suffix = args.dns_suffix
 description = args.description
 ip_address = args.IP_address
 tll = args.tll

 create_managed_zone = "gcloud dns managed-zones create "+ dns_name + " --dns-name=" + dns_suffix + " --description=" + description
 print 'creating the managed zone ...'
 subprocess.call([create_managed_zone], shell=True )
 print 'Adding the A record ...'
 add_A_record = "gcloud dns record-sets transaction add "+ ip_address + " --type=A --ttl=" + tll + " --zone="+ zone_name + " --name="+ dns_suffix 
 subprocess.call([add_A_record], shell=True )
 print 'Here the needed informations about the created zone:'
 describe_zone = "gcloud dns managed-zones describe " + zone_name
 subprocess.call([describe_zone], shell=True )

if __name__ == "__main__":
 main()
