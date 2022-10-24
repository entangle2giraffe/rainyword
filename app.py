import socket
import time
import configparser
import time
import logging
from player import json_players
import Object

# Logger Config
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s %(message)s')

def _read_config() -> int:
    config = configparser.ConfigParser()
    config.read("config") # Read config file
    port = config.get('server','port')
    
    return port

def init_server(client_n=2):
    """
    Open up TCP Socket Server
    """
    port = _read_config()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Initialize TCP
    sock.bind(('',int(port)))
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

def main():
    s = init_server()

    while True:
        # Establish connection
        c, addr = s.accept()
        # Send a text to the client
        c.sendall(f'Hi {str(addr)} {client_init()}'.encode())
        c.close
        #break

if __name__ == "__main__":
    main()
    