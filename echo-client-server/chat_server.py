from _thread import *
import threading
import socket
import time
import sys
from datetime import datetime
import os

MAX_CLIENTS = 10
client_list = []

my_lock = threading.Lock() 

def c_thread(conn,addr):
    for i in range(10):
        message = conn.recv(1024)
#        print(addr[0],":",message)
        if message:
            """
            ####
            have to print client_list here and ask user to give
            name of his friend to whom he wish to send message
            can implement broadcast also
            #####
            """
            print(addr[0],":",message)
        else: # removing
            if conn in client_list:
                client_list.remove(conn)
            




if __name__ == '__main__':
    s_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    if len(sys.argv) != 3:
        print("Incorrect format!\n")
        print("Correct Order : filename,IP,port number.")
        exit()
    ip_s   = str(sys.argv[1])
    port_s = int(sys.argv[2]) 
    s_soc.bind((ip_s,port_s))
    s_soc.listen(MAX_CLIENTS)
    print("In Listen mode..")
    

    while True:
        conn,addr = s_soc.accept()
        client_list.append(conn)
        print("connected to",addr[0])
        conn.send("Connected!You can send messages now..".encode())
        start_new_thread(c_thread,(conn,addr))
    conn.close()
    s_soc.close()


