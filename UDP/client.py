# UDP (User Datagram Protocol) is a connectionless protocol. It is a simple protocol that exchanges datagrams without
# acknowledgments or guaranteed delivery, requiring that error processing and retransmission be handled by other
# protocols. UDP is often used with time-sensitive applications, such as audio/video streaming and realtime gaming,
# where dropping some packets is preferable to waiting for delayed data. client.py is a simple UDP client that sends
# a message to the server and waits for a response. The client sends the message "Hello, Server" to the server and
# waits for a response. When the client receives a response, it prints the message to the console.

import socket
import datetime

IP = "localhost"  # "127.0.0.1"
PORT = 57000
MESSAGE = "Hello, Server"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    # Send a message to the server
    msg = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + MESSAGE
    client.sendto(msg.encode(), (IP, PORT))
    print(f"Sent {msg} to {IP}:{PORT}")

    # Wait for a response from the server
    data, addr = client.recvfrom(1024)
    print(f"Received {data.decode()} from {addr}")