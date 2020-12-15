from _thread import *
import threading
import socket
import time
import sys
from datetime import datetime


if __name__ == '__main__':

    ### METHOD 1
    
    # Creating server socket
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_host   = socket.gethostname()
    ip       = socket.gethostbyname(s_host)
    s_PORT   = 9999

    print("Your IP :",ip)
    s_host = input('Enter friend\'s IP address:')
    name = input('Enter Friend\'s name:')
    c_socket.connect((s_host,s_PORT))

    c_socket.sendall(name.encode())
    server_name = c_socket.recv(1024)
    server_name = server_name.decode()
    print('Connected with',server_name)

    while True:
        message = (c_socket.recv(1024)).decode()
        print(server_name,":",message)
        c_socket.sendall(message.encode())
        # data = c_socket.recv(1024)
        
        want = input('Say y/n:')
        if want == 'y':
            continue
        else:
            break
    c_socket.close()
    

    ### GFG METHOD
    #https://www.geeksforgeeks.org/simple-chat-room-using-python/
    