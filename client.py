import socket
import json
import configparser

# close connection of Socket with the server and return Socket
def close_connection(Socket: socket.SocketType) -> socket.SocketType:
    while True:
        Socket.sendall(f'exitNow'.encode())
        close = Socket.recv(1024).decode()
        if close == 'closeNow':
            Socket.sendall(f'closedNow'.encode())
            Socket.close
            break
    return Socket    

config = configparser.ConfigParser()
config.read("config")
s = socket.socket()
port = int(config.get('server','port'))
s.connect(('127.0.0.1',port))
print(s.recv(1024).decode())
close_connection(s)