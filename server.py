import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
BUFFER_SIZE = 4096

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)

print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, address = s.accept()

print(f"{address[0]}:{address[1]} Connected!")

with open("received_file.txt", "wb") as f:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)

client_socket.close()
s.close()


# import socket
# Server_ip="localhost"
# Server_host=8002
# FORMAT="utf-8"
# SS=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# SS.bind((Server_ip,Server_host))
# SS.listen(5)
# s1, addr=SS.accept()
# file_name= s1.recv(1024).decode(FORMAT)
# print(file_name)
# file=open(file_name,"w")
# s1.send("File name received")
# data=s1.recv(1024).decode(FORMAT)
# print("File data received")
# s1.send("File data received")
# file.write(data)
# file.close()