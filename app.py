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
    c, addr = s.accept()
    logging.debug("Connection from: "+str(addr))
    
    # recieve 
    data = c.recv(1024).decode() # recieve data from client
    logging.info(f"client: {str(data)}")
    c.sendall(f'{client_init()}'.encode()) # send back player json
    # Simulated data sending
    while True:
        data = c.recv(1024).decode()
        if not data: break
        logging.info(f"{addr}: {str(data)}")
        data = input('->')
        c.send(data.encode())
    c.close

if __name__ == "__main__":
    main()
    