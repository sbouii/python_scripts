import socket
s = socket.socket()
#put the server port 
port = 25631
#connect to the server from local computer
s.connect(('127.0.0.1', port))
#receive data from the server
print s.recv(1024) 
# close the connection
s.close()
