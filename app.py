import socket
import time
import logging
import reciever.lobby as lobby
import sender.player as player
import sender.word_list as wl
import Object
import os
from _thread import *
from threading import Thread
import json

class Server:
    connections = []
    addresses = []
    threads = []
    thread_count = 0
    FORMAT = "utf-8"

    def __init__(self, port:int):        
        logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s %(message)s')
        self.port = port
  
    def broadcast(self, client1, client2):
        """
        Broadcast msg to 2 clients
        """
        for conn in [client1, client2]:
            conn.send(msg.encode(self.FORMAT))

    def announce(self):
        """
        Announce msg to entire lobby
        """
        for conn in self.connections:
            conn.sendall(msg.encode(self.FORMAT))

    def word_gen(self, client1, client2):
        """
        Generates 5 words every 3 seconds for the period of 
        5 minute
        """
        countdown_thread = Thread(target=wl.countdown)
        countdown_thread.start()
        while wl.my_timer > 0:
            self.broadcast(wl.generate_random_words(), client1, client2)
            time.sleep(3)

    def threaded_recieve(self, c):
        """
        Make the client able to send data while recieve it from
        the server
        """
        while True:
            try:
                message = c.recv(1024).decode(self.FORMAT)
                print(message)
            except:
                c.close()
                break

    def multi_threaded_client(self, c:socket, new_client):
        """
        Connect Multiple CLients in Python
        """
        DISCONNECT_MESSAGE = "!DISCONNECT" # [NOT IMPLEMENT]
        player_ID = self.thread_count # player assigned id in each thread
        isBusy = False #placeholder

        c.sendall(f'{player.assign_id(player_ID)}'.encode(self.FORMAT)) # send an assigned id to client
        player.add_to_list(player_ID, new_client, isBusy) # add this client to player_list
        while True:
            data = c.recv(2048).decode()
            if data == '{"requestPlayerList": ' + str(player_ID) + '}':
                c.sendall(f'{player.send_player_list()}'.encode(self.FORMAT))# send player_list to the client
            if not data:
                break
        recv_thread = Thread(target=self.threaded_recieve, args=(c,))
        recv_thread.start()
        threads.append(recv_thread)
        self.word_gen()    
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
                self.c, self.addr = sock.accept() #accept connection from a client
            except:
                break
            self.connections.append(self.c)
            self.addresses.append(self.addr)
            new_client = json.loads(self.c.recv(2048).decode())
            logging.debug(new_client) # {'newClient': 'Alice'}
            logging.debug(type(new_client)) # dict
            logging.debug(new_client['newClient']) # Alice
            print("") 
            #print(self.connections)
            #print(self.addresses) 
            logging.debug("Connection from: "+str(self.addr))
            start_new_thread(self.multi_threaded_client,(self.c, new_client['newClient'])) #use current self.c to start a new thread
            self.thread_count += 1
            logging.debug(f"Thread: {self.thread_count}")
            #logging.debug(f"connections[] length: " + str(len(self.connections))) 
            print("")
        logging.info("socket is closed")
        sock.close()
    
if __name__ == '__main__':
    s = Server(6969)
    s.start(10)
