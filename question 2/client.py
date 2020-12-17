import socket
import sys

s_PORT   = 9999

# Creating client socket
#only ipv4
c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if(len(sys.argv) != 2):
	print("format: <filename> <server name>")
	sys.exit()
name = sys.argv[1]
allhostinfo = socket.getaddrinfo(name, s_PORT)
# print(allhostinfo)
hostinfo, _, _ = allhostinfo
s_host = hostinfo[4]
c_socket.connect(s_host)

while True:
    query=input("want to run a cmd ? y/n ")
    if query=='n':
        break
    command=input("Enter the cmd : ")
    if not command:
    	continue
    c_socket.send(command.encode())    
    print("sent ", command)

    output=c_socket.recv(2048).decode()
    print("output of cmd:\n"+output)



c_socket.close()