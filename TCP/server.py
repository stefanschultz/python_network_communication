# TCP (Transmission Control Protocol) is a connection-oriented protocol. It is a reliable, stream-oriented protocol
# that provides a full-duplex communication channel. TCP is often used with applications that require high
# reliability, such as web browsers, email clients, and file transfer applications. server.py is a simple TCP server
# that listens for incoming TCP connections on port 57000. When a client connects to the server, the server sends a
# response back to the client with the message "Hello, Client".

import socket
import datetime

IP = "localhost"  # "127.0.0.1"
PORT = 57000
MESSAGE = "Hello, Client"

with socket.create_server((IP, PORT)) as server:
    print(f"Server is listening on {IP}:{PORT}")

    # Listen for incoming TCP connections
    server.listen(1)

    # Accept a connection from a client
    conn, addr = server.accept()
    with conn:
        print(f"Connected to {addr}")

        # Receive data from the client
        data = conn.recv(1024)
        print(f"Received {data.decode()} from {addr}")

        # Send a message to the client
        msg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + MESSAGE
        conn.sendall(msg.encode())
        print(f"Sent {msg} to {addr}")
