from _thread import *
import threading
import socket
import time
import sys
from datetime import datetime

MAX_CLIENTS = 10
client_list=[]

#my_lock = threading.Lock() 

def threaded(conn,name):
    while True:
        message = conn.recv(1024)
        if not message:
            print(name+" connection closed")
            break
        message=name.encode()+" :".encode()+message
        for connec in client_list:
            if connec!=conn:
                connec.send(message)

        
        
    conn.close()
    client_list.remove(conn)

#    my_lock.release()
        



if __name__ == '__main__':

    s_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating socket
    s_hostname = socket.gethostname() # retrieving hostname
    s_ip = socket.gethostbyname(s_hostname) # get ip of host
    port = 9990
    s_soc.bind((b'',port)) #binding host to port
    print("IP of server :",s_ip)
    name = input('Enter name of Server:')
    s_soc.listen(MAX_CLIENTS)
    print("In Listen mode..")

    
    while True:
#        my_lock.acquire()
        conn, add = s_soc.accept() # accepting connection
        print(conn) 
        print("Received connection from ", add[0]) # add - IP address of client
        print('Connection Established. Connected From: ',add[0])
        c_message = conn.recv(1024)
        name_of_client=c_message.decode()
        print("Name of client: ",name_of_client)
        client_list.append(conn)
        conn.send(name.encode())
        start_new_thread(threaded, (conn,name_of_client))
    s_soc.close()


