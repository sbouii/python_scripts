### Setup:
- This script automate the creation of a managed zone on Google cloud platform using gcloud and then add an A record that resolves to an IP address.

### Steps:

 ` python deploy_dns.py --zone_name "myzone" --dns_suffix "example.com." --description "zone description" --ip_address "1.2.3.4" --tll 1234 `

