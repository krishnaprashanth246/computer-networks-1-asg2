import socket
import sys 
import time
from datetime import datetime

PORT = 12457

oursocket = socket.socket(type=socket.SOCK_STREAM)
print ("Socket successfully created") 


#oursocket.bind(('', PORT))        
#print ("socket binded to {}".format(PORT))

ip = sys.argv[1]
_, _, hostinfo = socket.getaddrinfo(ip,9999)

print(hostinfo)
_,_,_,_,(hostid, hostport) = hostinfo


# while True:
oursocket.connect((hostid, hostport))  
systime = "client's systime "
currtime = datetime.now()
dt_string = currtime.strftime("%d/%m/%Y %H:%M:%S")
systime += dt_string
# receive data from the server  
oursocket.send(systime.encode('utf-8'))
print("msg from server: ",oursocket.recv(1024))
# close the connection  
#time.sleep(1)
oursocket.shutdown(socket.SHUT_RDWR)
oursocket.close()
