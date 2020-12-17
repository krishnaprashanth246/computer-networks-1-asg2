import socket
import sys

s_PORT   = 9999

# Creating client socket

if(len(sys.argv) != 2):
	print("format: <filename> <server name>")
	sys.exit()
name = sys.argv[1]
allhostinfo = socket.getaddrinfo(name, s_PORT)
# print(allhostinfo)
hostinfo, _, _ = allhostinfo
s_host = hostinfo[4]
if len(s_host) == 2:
	c_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	c_socket.connect(s_host)
elif len(s_host) == 4:
	c_socket = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
	c_socket.connect((s_host[0],s_host[1],0,0))
# c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# c_socket.connect(s_host)
print("want to run a command :")
print("type y for yes")
print("type n for no")
print()
while True:
    query=input("enter option(y/n) : ")
    if query=='n':
        break
    command=input("Enter the cmd : ")
    if not command:
    	continue
    c_socket.send(command.encode())    
    print("sent ", command)

    output=c_socket.recv(2048).decode()
    print("------------------------")
    print("output of cmd: \n"+output + "------------------------")
c_socket.close()