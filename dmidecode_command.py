import subprocess
import optparse

def system_info():
 command = "dmidecode"
 p = optparse.OptionParser(description="Python 'dmidecode' clone")
 p.add_option("-t", "--table", help="Extract hardware information by reading data from the DMI tables")
 options, arguments = p.parse_args()
 
 print "Gathering %s information..." % options.table
 subprocess.call([command, "-t", options.table])
    
def main():
 system_info()

if __name__ == "__main__":
 main()
