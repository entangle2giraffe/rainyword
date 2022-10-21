import socket
import json
import configparser

config = configparser.ConfigParser()
config.read("config")
s = socket.socket()
port = int(config.get('server','port'))
s.connect(('127.0.0.1',port))
print(s.recv(1024).decode())
s.close()