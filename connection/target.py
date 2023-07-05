import socket
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from get_temp import readSensor
# from get_temp import readSensor
target_ip = "192.168.4.1"
target_port = 3334
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, target_port))

message = str(readSensor())  # 送信するメッセージ文字列
s.send(message.encode("utf-8"))  # メッセージをエンコードして送信

response = s.recv(buffer_size)
print(response.decode("utf-8"))

s.close()
