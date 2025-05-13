I was studying how DNS works, but it turns out I need to know how socket works first. I am sharing this with you as it may be helpful for you.





## So, what is a Socket? 

A socket in networking is an endpoint for communication between two machines over the network. You can think of it as a pipe between the two devices. A combination of IP address + Port number is used to establish the connection. Think of it like a home address and the door number where a message should go.





## Sockets are of two major types:

**Stream Sockets:** Use TCP, for a reliable connection, like loading a website.

**Datagram Sockets:** Use UDP, for unreliable but faster connections,  such as video streaming.



## How does it work?

A Socket Requires a Server and a client to establish a connection. 

Firstly, the client sends a  SYN to the server. In reply, the server returns a SYN-ACK to the client. Then again, the client sends ACK to the server and they get connected. 

Too complicated? Hu? Let's make it simpler.

Imagine two people want to chat:

P1->P2: 👋 “Hello, are you there?”

P2->P1: 🤝 “Yes, I’m here. Are you ready?”

P1->P2:  ✅ “I’m ready!”



Yes, that's simple. This is not Rocket science, just some geeky stuff! 😵‍💫


```
Client ---------------------------------------------- Server

 | ------------------ SYN (Seq=1000) ------------------> |

 | <----------- SYN-ACK (Seq=2000, Ack=1001) ----------- |

 | ------------------- ACK (Ack=2001) -----------------> |

 | ---------------- Connection Ready -------------------> |
```


When a socket connection is opened in Unix-like system, it returns a file descriptor - just open() does for a file. (Note: A file descriptor is an integer handle used by the OS to identify and manage open I/O resources.





In Python, it's straightforward to create a Socket.

Server

-------
```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET: IPv4 , SOCK_STREAM: TCP socket

server.bind(("localhost", 8000))

server.listen(1) # number connection can be queued

conn, addr = server.accept()

data = conn.recv(1024)

print("Received:", data.decode())

conn.send("Hello Client".encode())

conn.close()
```


Client

------
```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 8000))

client.send("Hello Server".encode())

data = client.recv(1024)

print("Received:", data.decode())

client.close()

```

### This repo contains a simple socket connection and a file transfer server-client setup code.
