import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000
BUFFER_SIZE = 4096
FILE_PATH = 'data/abc.txt'

s = socket.socket()

s.connect((SERVER_HOST, SERVER_PORT))

with open(FILE_PATH, 'rb') as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        s.sendall(bytes_read)

s.close()


# import socket
# Server_ip="localhost"
# Server_host=8002
# FORMAT="utf-8"
# CS=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# CS.connect((Server_ip,Server_host))
# file = open("data/abc.txt","r")
# data=file.read()
# CS.send("abc.txt".encode(FORMAT))
# msg=CS.recv(1024)
# print( msg)
# CS.send(data.encode(FORMAT))
# msg=CS.recv(1024)
# print(msg)