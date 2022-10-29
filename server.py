import socket 
import os 
from _thread import *
import configparser
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s %(message)s')
config = configparser.ConfigParser()
ThreadCount = 0

def init():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initialize TCP
    port = 6969

    try:
        sock.bind(('',int(port)))
    except socket.error as e:
        print(str(e))
    logging.info('Socket is listening..') 
    sock.listen(2)

    return sock 

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()


while True:
    sock= init()
    conn, addr = sock.accept()
    logging.debug(f'Connection from {addr}')
    
    start_new_thread(multi_threaded_client, (conn, ))
    ThreadCount += 1
    logging.debug(f'Thread Number: {str(ThreadCount)}')
sock.close()
