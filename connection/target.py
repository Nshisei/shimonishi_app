import socket
import sys
import os
# from get_temp import readSensor
target_ip = "192.168.4.3"
target_port = 3334
buffer_size = 1024

def get_temp_from_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))
    response = s.recv(buffer_size)
    return response.decode("utf-8")
    s.close()
