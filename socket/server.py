import socket
s = socket.socket()
print "Socket successfully created!"
port = 25631
#the server listens from diffrent ip addresses
s.bind(('', port))
print "Socket binded to %s" %(port)
s.listen(5)
print "Socket is listening"
while True
 c, addr = s.accept()
 print 'Got connection fron', addr
 c.send('Connection accepted!')
 c.close()
