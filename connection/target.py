import socket
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from get_temp import readSensor
# from get_temp import readSensor
target_ip = "192.168.4.3"
target_port = 3334
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, target_port))
response = s.recv(buffer_size)
print(response.decode("utf-8"))

s.close()
