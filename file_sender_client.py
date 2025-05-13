import socket
import os
SERVER_HOST = 'localhost'
SERVER_PORT = 5001
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

filename = "demo_f.txt"
filesize = os.path.getsize(filename)

client_socket = socket.socket()
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"+ Connected to {SERVER_HOST}:{SERVER_PORT}")

client_socket.send(f"{os.path.basename(filename)}{SEPARATOR}{filesize}".encode())

with open(filename, "rb") as f:
    while True:
        data = f.read(BUFFER_SIZE)
        if not data:
            break
        client_socket.sendall(data)

print("file sent successfully.")
client_socket.close()
