from _thread import *
import threading
import socket
import time
import sys
from datetime import datetime

MAX_CLIENTS = 10

#my_lock = threading.Lock() 

def threaded(conn):
    while True:
        message = conn.recv(1024)
        if not message:
            print('Ba byee!')
            break
        message += b" received"
        conn.send(message)
    conn.close()
#    my_lock.release()
        



if __name__ == '__main__':

    s_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating socket
    s_hostname = socket.gethostname() # retrieving hostname
    s_ip = socket.gethostbyname(s_hostname) # get ip of host
    port = 9999
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
        print("Name of client: ",c_message.decode())
        conn.sendall(name.encode())
        start_new_thread(threaded, (conn,))
    s_soc.close()


