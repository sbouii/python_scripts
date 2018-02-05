import sys, os
# create fork from the parent script
pid = os.fork()

if pid > 0:
   # exit parent process
  sys.exit(0)

else:
   # create a new process group using setsid()
   # the child process becomes the leader of the new process group
   os.setsid()
   # run the child process under root directory
   os.chdir("/")
   # forward input and output source(standard file descriptors) to /dev/null
   sys.stdout=open("/dev/null", 'w')
   sys.stdin=open("/dev/null", 'r')
   while(1):
     print "it's a python daemon"
