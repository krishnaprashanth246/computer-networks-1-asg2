import socket
import sys
import time
from datetime import datetime


PORT = 9999 

oursocket = socket.socket(type=socket.SOCK_STREAM)
print ("Socket successfully created") 


oursocket.bind((b'', PORT))        
print ("socket binded to {}".format(PORT))  
  
# put the socket into listening mode  
oursocket.listen(5)   
print ("socket is listening")            

while True:  
    c, addr = oursocket.accept()      
    print ('Got connection from', addr ) 
    systime = "Server's systime "
    currtime = datetime.now()
    dt_string = currtime.strftime("%d/%m/%Y %H:%M:%S")
    systime += dt_string
    ret = c.recv(1024)
    print('return message from client: ', ret)
    c.send(systime.encode('utf-8'))  

    c.close()

