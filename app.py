import socket
import time
import logging
from sender.player import json_players
import Object
import os
from _thread import *
from sender.assign_id import return_id

class Server:
    connections = []
    addresses = []
    thread_count = 0

    def __init__(self, port:int):        
        logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s %(message)s')
        self.port = port
  
    def multi_threaded_client(self):
        """
        Connect Multiple CLients in Python
        """
        FORMAT = "utf-8"
        DISCONNECT_MESSAGE = "!DISCONNECT" # [NOT IMPLEMENT]
        #connection.send(str.encode(f'Server is working:'))
        #data = connection.recv(2048)
        #logging.info(f'{address} '+data.decode(FORMAT))
        #response = client_init()
        #connection.sendall(f'{response}'.encode(FORMAT))
        self.c.sendall(f'{return_id(self.thread_count)}'.encode(FORMAT))
        while True:
            data = self.c.recv(2048)
            response = '[SERVER] ' +data.decode(FORMAT)
            if not data:
                break
            try:
                self.c.sendall(str.encode(response))
            except:
                break

        self.c.close()

    def start(self, client_n:int=2):
        """
        Open up TCP Socket Server
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Initialize TCP
        try:
            sock.bind(('',self.port))
        except socket.error as e:
            logging.error(f"{str(e)}")
        logging.info(f"socket is binded to {self.port}")

        # listen to n clients 
        sock.listen(client_n)
        logging.info("socket is listening")
        while True:
            try:
                self.c, self.addr = sock.accept()
            except:
                break
            self.connections.append(self.c)
            self.addresses.append(self.addr) 
            logging.debug("Connection from: "+str(self.addr))
            start_new_thread(self.multi_threaded_client,())
            self.thread_count += 1
            logging.debug(f"Thread: {self.thread_count}")
        sock.close()
        
def client_init():
    """
    When client send first two data about players
    """
    p1 = Object.Player(1)
    p2 = Object.Player(2)
    data = json_players(p1,p2)
    return data


if __name__ == '__main__':
    s = Server(6969)
    s.start() 
