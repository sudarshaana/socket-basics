import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8000))
client.send("Hello Server".encode())
data = client.recv(1024)
print("Received:", data.decode())
client.close()
