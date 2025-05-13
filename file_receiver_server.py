import socket

SERVER_HOST = 'localhost'
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

server_socket = socket.socket()
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print(f"* Listening on {SERVER_HOST}:{SERVER_PORT}")

client_socket, address = server_socket.accept()
print(f"{address} connected")

received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
filename = "received_" + filename
filesize = int(filesize)
print(f"receiving {filename} ({filesize} bytes)")

with open(filename, "wb") as f:
    bytes_read = 0
    while bytes_read < filesize:
        data = client_socket.recv(BUFFER_SIZE)
        if not data:
            break
        f.write(data)
        bytes_read += len(data)

print("file received ")
client_socket.close()
server_socket.close()
