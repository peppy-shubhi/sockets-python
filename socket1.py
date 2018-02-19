import socket

s = socket.socket()
host = socket.gethostname()
port = 9077
s.bind((host,port))
s.listen(5)

while True:
    c, addr = s.accept()
    print("Connection accepted from " + repr(addr[1]))
    c.sendall(b'Thank you for connecting')
    c.close()
