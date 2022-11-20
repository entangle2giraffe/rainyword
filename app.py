import socket
import time
import logging
import reciever.lobby as lobby
import sender.player as player
import Object
import os
from _thread import *
import threading

class Server:
    connections = []
    addresses = []
    thread_count = 0

    def __init__(self, port:int):        
        logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s %(message)s')
        self.port = port
        self.lb = lobby.Lobby("status.json")
  
    def multi_threaded_client(self, c:socket):
        """
        Connect Multiple CLients in Python
        """
        FORMAT = "utf-8"
        DISCONNECT_MESSAGE = "!DISCONNECT" # [NOT IMPLEMENT]
        
        c.sendall(f'{player.assign_id(self.thread_count)}'.encode(FORMAT))
        # Read player status
        data = c.recv(2048) 
        self.lb.read_status(data)
        c.sendall(b"Game Started")
        # lobby.return_player() -> Game start here
        # sender.word_list
        # typed_word
        # expired_word
        while True:
            data = c.recv(2048)
            response = '[SERVER] ' + data.decode(FORMAT)
            if not data:
                break
            try:
                c.sendall(str.encode(response))
            except:
                break

        c.close()

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
            print("") 
            print(self.connections)
            print(self.addresses) 
            logging.debug("Connection from: "+str(self.addr))
            start_new_thread(self.multi_threaded_client,(self.c,)) #use current self.c to start a new thread
            self.thread_count += 1
            logging.debug(f"Thread: {self.thread_count}")
            logging.debug(f"connections[] length: " + str(len(self.connections))) 
            print("")
        logging.info("socket is closed")
        sock.close()
        self.lb.reset_dict()
        
    
if __name__ == '__main__':
    s = Server(6969)
    s.start()
