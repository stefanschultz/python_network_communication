# UDP (User Datagram Protocol) is a connectionless protocol. It is a simple protocol that exchanges datagrams without
# acknowledgments or guaranteed delivery, requiring that error processing and retransmission be handled by other
# protocols. UDP is often used with time-sensitive applications, such as audio/video streaming and realtime gaming,
# where dropping some packets is preferable to waiting for delayed data. server.py is a simple UDP server that
# listens for incoming UDP packets on port 57000. When a packet is received, the server sends a response back to the
# client with the message "Hello, Client".

import socket
import datetime

IP = "localhost"  # "127.0.0.1"
PORT = 57000
MESSAGE = "Hello, Client"

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    # Bind to the IP and port
    server.bind((IP, PORT))
    print(f"Server is listening on {IP}:{PORT}")

    # Listen for incoming UDP packets
    while True:
        data, addr = server.recvfrom(1024)
        print(f"Received {data.decode()} from {addr}")
        msg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + MESSAGE
        server.sendto(msg.encode(), addr)