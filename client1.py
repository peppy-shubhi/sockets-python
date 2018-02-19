import socket

s = socket.socket()
host = socket.gethostname()
port = 9077
s.connect((host, port))
print (s.recv(1024))
