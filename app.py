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

class Server:
    connections = []
    addresses = []
    threads = []
    word_list_dict = {}
    score_dict = {}
    thread_count = 0
    listening = False
    FORMAT = "utf-8"

    def __init__(self, port:int):        
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(1)
        f_handler = logging.FileHandler('app.log')
        c_handler = logging.StreamHandler()
        
        formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s')
        c_handler.setFormatter(formatter)
        f_handler.setFormatter(formatter)
        for h in (c_handler,f_handler):
            self.logger.addHandler(h)
        #logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s %(message)s')
        self.port = port
        self.lb = lobby.Lobby("status.json")
    
    # check all the time if there is any matched request every 1 sec. If so, send matchStart message to two matched clients ex.{"matchStart":[1,123]}
    def match_request_check(self):
        while self.listening == True: # exit while loop when the server stopped listening
            matched = request.check_request()
            if matched != 0: 
                c1 = player.find(matched[0])
                c2 = player.find(matched[1])
                message = '{"matchStart":' + str(matched) + '}'
                self.broadcast(message, self.connections[c1], self.connections[c2]) 
                matched = 0
                self.logger.debug("matched!!!")
            time.sleep(1)
        self.logger.debug("match_request_check has stopped working")    
  
    def broadcast(self, msg):
        for conn in self.connections:
            conn.send(msg.encode("utf-8"))

    def multi_threaded_client(self):
        """
        Connect Multiple CLients in Python
        """
        FORMAT = "utf-8"
        DISCONNECT_MESSAGE = "!DISCONNECT" # [NOT IMPLEMENT]
        self.c.sendall(f'{player.assign_id(self.thread_count)}'.encode(FORMAT))
        # Read player status
        data = self.c.recv(2048) 
        #self.lb.read_status(data)
        self.c.sendall("Game Started".encode(FORMAT))
        self.word_gen()
        # lobby.return_player() -> Game start here
        # sender.word_list
        # typed_word
        # expired_word
        #while True:
            #data = self.c.recv(2048)
            #response = '[SERVER] ' +data.decode(FORMAT)
            #if not data:
                #break
            #try:
                #self.c.sendall(str.encode(response))
            #except:
                #break

        self.c.close()

    def word_gen(self):
        countdown_thread = Thread(target=wl.countdown)
        countdown_thread.start()
        while wl.my_timer > 0:
            self.broadcast(wl.generate_random_words())
            time.sleep(3)


    def start(self, client_n:int=2):
        """
        Open up TCP Socket Server
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Initialize TCP
        try:
            sock.bind(('',self.port))
        except socket.error as e:
            self.logger.error(f"{str(e)}")
        self.logger.info(f"socket is binded to {self.port}")

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
    
if __name__ == '__main__':
    s = Server(6969)
    s.start() 
