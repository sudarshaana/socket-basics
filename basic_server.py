import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8000))
server.listen(1)
print("Waiting for client...")
conn, addr = server.accept()
print(f"Connected by {addr}")
data = conn.recv(1024)
print("Received:", data.decode())
conn.send("Hello Client".encode())
conn.close()
