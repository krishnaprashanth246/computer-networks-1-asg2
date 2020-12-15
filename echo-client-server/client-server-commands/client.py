import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",4444))

while True:
    query=input("want to run a cmd ? y/n ")
    if query=='n':
        break
    command=input("Enter the cmd : ")
    client.send(command.encode())
    output=client.recv(2048).decode()
    print("output of cmd:"+output)



client.close()