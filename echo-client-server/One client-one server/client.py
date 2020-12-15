import socket
import sys
from datetime import datetime

# Creating server socket
c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s_host   = socket.gethostname()
#ip       = socket.gethostbyname(s_host)
s_PORT   = 9999

#print("Your IP :",ip)
#s_host = input('Enter friend\'s IP address:')
name = input('Enter Friend\'s name:')
allhostinfo = socket.getaddrinfo(name, s_PORT)
# print(allhostinfo)
hostinfo, _, _ = allhostinfo
s_host = hostinfo[4]
c_socket.connect(s_host)

c_socket.sendall("Client".encode())
server_name = c_socket.recv(1024)
server_name = server_name.decode()
print('Connected with',server_name)

while True:
    message = input('Client:')
    c_socket.sendall(message.encode())
    if message == 'close': #exit from loop if 'close' is encountered
        break
    message = (c_socket.recv(1024)).decode()
    print(server_name,":",message)
    #c_socket.sendall(message.encode())
c_socket.close()