import socket
import sys
import time
from datetime import datetime

PORT = 12457

oursocket = socket.socket(type=socket.SOCK_STREAM)
print("Socket successfully created")


#oursocket.bind(('', PORT))
#print ("socket binded to {}".format(PORT))

ip = sys.argv[1]
allhostinfo = socket.getaddrinfo(ip, 9999)
# print(allhostinfo)
hostinfo, _, _ = allhostinfo
ipv = hostinfo[0]
print(ipv)
if ipv == socket.AF_INET:  # IPv4
    (hostid, hostport) = hostinfo[4]
    oursocket.connect((hostinfo[4]))
else:
    (hostid, hostport, flowinfo, scope_id) = hostinfo[4]
    oursocket.connect((hostid, hostport, 0, 0))
print(hostinfo[4])
#_, _, _, _, (hostid, hostport) = hostinfo


# while True:

systime = "client's systime "
currtime = datetime.now()
dt_string = currtime.strftime("%d/%m/%Y %H:%M:%S")
systime += dt_string
for i in range(1024 - len(systime)):
    systime += 'a'
for i in range(len(systime)):
    systime += 'b'
# receive data from the server
oursocket.send(systime.encode('utf-8'))
print("msg from server: ", oursocket.recv(1024))
# close the connection
# time.sleep(1)
# oursocket.shutdown(socket.SHUT_RDWR)
oursocket.close()
