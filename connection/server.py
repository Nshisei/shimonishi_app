import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import socket
from get_temp import readSensor
server_ip = "192.168.4.3"
server_port = 3334
listen_num = 5
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server_ip, server_port))
s.listen(listen_num)
while True:
    client, address = s.accept()
    print(f"Connection from {address} is established")
    message = str(readSensor())
    client.send(bytes(message, 'utf-8'))
    client.close()
