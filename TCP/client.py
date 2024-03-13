# TCP (Transmission Control Protocol) is a connection-oriented protocol. It is a reliable, stream-oriented protocol
# that provides a full-duplex communication channel. TCP is often used with applications that require high
# reliability, such as web browsers, email clients, and file transfer applications. client.py is a simple TCP client
# that connects to a server and sends a message. The client sends the message "Hello, Server" to the server and waits
# for a response. When the client receives a response, it prints the message to the console.

import socket
import datetime

IP = "localhost"  # "127.0.0.1"
PORT = 57000
MESSAGE = "Hello, Server"

with socket.create_connection((IP, PORT)) as client:
    # Send a message to the server
    msg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + MESSAGE
    client.sendall(msg.encode())
    print(f"Sent {msg} to {IP}:{PORT}")

    # Wait for a response from the server
    data = client.recv(1024)
    print(f"Received {data.decode()} from {IP}:{PORT}")