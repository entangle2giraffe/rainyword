import socket
import time
import logging
import reciever.lobby as lobby
import sender.player as player
import Object
import os
from _thread import *

class Server:
    connections = []
    addresses = []
    thread_count = 0

    def __init__(self, port:int):        
        logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s %(message)s')
        self.port = port
        self.lb = lobby.Lobby("status.json")
  
    def multi_threaded_client(self):
        """
        Connect Multiple CLients in Python
        """
        FORMAT = "utf-8"
        DISCONNECT_MESSAGE = "!DISCONNECT" # [NOT IMPLEMENT]
        self.c.sendall(f'{player.assign_id(self.thread_count)}'.encode(FORMAT))
        # Read player status
        data = self.c.recv(2048) 
        self.lb.read_status(data)
        self.c.sendall("Game Started")
        # lobby.return_player() -> Game start here
        # sender.word_list
        # typed_word
        # expired_word
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
            print(self.connections)
            print(self.addresses) 
            logging.debug("Connection from: "+str(self.addr))
            start_new_thread(self.multi_threaded_client,())
            self.thread_count += 1
            logging.debug(f"Thread: {self.thread_count}")
        sock.close()
        self.lb.reset_dict()
        
    
if __name__ == '__main__':
    s = Server(6969)
    s.start() 
