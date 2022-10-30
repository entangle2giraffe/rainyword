import socket
import time
import configparser
import time
import logging
from player import json_players
import Object
import os
from _thread import *

# Logger Config
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s %(message)s')

def _read_config() -> int:
    config = configparser.ConfigParser()
    config.read("config") # Read config file
    port = config.get('server','port')
    
    return port

def start(client_n=2):
    """
    Open up TCP Socket Server
    """
    port = _read_config() # Read config file
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Initialize TCP
    try:
        sock.bind(('',int(port)))
    except socket.error as e:
        logging.error(f"{str(e)}")
    logging.info(f"socket is binded to {port}")

    # listen to n clients 
    sock.listen(client_n)
    logging.info("socket is listening")
    
    return sock

def client_init():
    """
    When client send first two data about players
    """
    p1 = Object.Player(1)
    p2 = Object.Player(2)
    data = json_players(p1,p2)
    return data

def multi_threaded_client(connection, address):
    """
    Connect Multiple CLients in Python
    """
    FORMAT = "utf-8"
    DISCONNECT_MESSAGE = "!DISCONNECT" # [NOT IMPLEMENT]

    #connection.send(str.encode(f'Server is working:'))
    data = connection.recv(2048)
    logging.info(f'{address} '+data.decode(FORMAT))
    response = client_init()
    connection.sendall(f'{response}'.encode(FORMAT))
    while True:
        data = connection.recv(2048)
        response = '[SERVER] ' +data.decode(FORMAT)
        if not data:
            break
        connection.sendall(str.encode(response))

    connection.close()

def main():
    thread_count = 0
    s = start()
    while True:
        c, addr = s.accept()
        logging.debug("Connection from: "+str(addr))
        start_new_thread(multi_threaded_client, (c,addr))
        thread_count += 1
        logging.debug(f"Thread: {thread_count}")
    s.close()

if __name__ == "__main__":
    main() 
