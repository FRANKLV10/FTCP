import socket
import time

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 8900))
while True:
    c.send(b"hello")

    data = c.recv(1024).decode()
    print(data)
