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
import sender.match_request as request
import typed_word as typed
import expired_word as remove
import utils
import exit

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
  
    def broadcast(self, msg, client1, client2):
        """
        Broadcast msg to 2 clients
        """
        for conn in [client1, client2]:
            conn.send(msg.encode(self.FORMAT))

    def announce(self, msg):
        """
        Announce msg to entire lobby
        """
        for conn in self.connections:
            conn.sendall(msg.encode(self.FORMAT))

    def word_gen(self, client1, client2, id1, id2):
        """
        Generates 5 words every 3 seconds for the period of 
        5 minute
        """
        id_lower = min(id1, id2)      
        if id_lower not in self.word_list_dict:
            self.word_list_dict[id_lower] = []
        for i in range(9):
            words = json.loads(wl.generate_random_words(25)) # {"word": ["adopt", "blacks", "personals", "coat", "guided"]}
            for i in words["words"]:
                self.word_list_dict[id_lower].append(str(i))
            #self.broadcast(utils.jsonify(words), client1, client2)
            client1.sendall(f'{utils.jsonify(words)}'.encode(self.FORMAT))
            client2.sendall(f'{utils.jsonify(words)}'.encode(self.FORMAT))
            time.sleep(0.5)

    def threaded_recieve(self, c1, c2, stop, id1, id2):
        """
        Make the client able to send data while recieve it from
        the server
        """
        lower_id = min(id1, id2)
        while True:
            #try:
                message = json.loads(c1.recv(2048).decode())
                if message == 'none':
                    break
                if "playerTyped" in message:
                    print(message)
                    print(self.word_list_dict)
                    typed_word = message["playerTyped"]
                    print(typed_word)
                    if typed_word in self.word_list_dict[lower_id]: # if typed correctly
                        mes = '{"wordRemoved":' +'"'+str(typed_word) + '"' +'}' 
                        self.word_list_dict[lower_id].remove(typed_word)
                        self.broadcast(mes, c1, c2)
                        self.score_dict[id1] += 1
                        score = '{"scoreList":[{"id":' + str(id1) + ',"score":' + str(self.score_dict[id1]) + "}]}"
                        print(score)
                        self.broadcast(score, c1, c2)
                        #{"scoreList":[{"id":0,"score":100}]}
                if "wordExpire" in message:
                    expired_word = message["wordExpire"]
                    if expired_word in self.word_list_dict[lower_id]:
                        self.word_list_dict[lower_id].remove(expired_word)
                #if "removeClient" in message: # ex. {"removeClient":1}
                    #c1.close()
                    #exit.quit(message["removeClient"])
                    #break
            #except:
               # c1.close()
                #exit.quit(id1)
                #print("error")
                #break

    #def start_game()        

    def multi_threaded_client(self, c:socket, new_client):
        """
        Connect Multiple CLients in Python
        """
        #try:
        DISCONNECT_MESSAGE = "!DISCONNECT" # [NOT IMPLEMENT]
        player_ID = self.thread_count # player assigned id in each thread
        isBusy = False #placeholder
        bla = True

        c.sendall(f'{player.assign_id(player_ID)}'.encode(self.FORMAT)) # send an assigned id to client
        player.add_to_list(player_ID, new_client, isBusy) # add this client to player_list
        # in lobby
        while True:
            data = json.loads(c.recv(2048).decode())
            # send player_list to the client
            if "requestPlayerList" in data: # ex.{"requestPlayerList":1}
                c.sendall(f'{player.send_player_list()}'.encode(self.FORMAT))
            # add matching request to the list match_request then send request to the opponent   
            if "matchRequest" in data:
                request.add_request(data["matchRequest"][0], data["matchRequest"][1])
                receiver = player.find(data["matchRequest"][1])
                self.connections[receiver].sendall(f'{str(data)}'.encode(self.FORMAT)) 
            if "readyToPlay" in data: # {"readyToPlay":[1,2]}
                my_id = data["readyToPlay"][0]
                opponent_id = data["readyToPlay"][1]
                myConnection = self.connections[player.find(my_id)] 
                opponentConnection = self.connections[player.find(opponent_id)]
                break
            #if "removeClient" in data: # ex. {"removeClient":1}
                #c.close()
                #exit.quit(player_ID)
            if not data:
                print("not data")
                break
        try: 
            if my_id not in self.score_dict:
                self.score_dict[my_id] = 0
        except:
            print("room creation error")
        stop_threads = False # recv_thread parameter for killing the thread
        recv_thread = Thread(target=self.threaded_recieve, args=(myConnection, opponentConnection,lambda: stop_threads, my_id, opponent_id))
        recv_thread.start() # thread_receive function
        self.threads.append(recv_thread)
        self.word_gen(myConnection, opponentConnection, my_id, opponent_id) # Generate words list and send to two clients
        myConnection.recv(2048).decode()
        stop_threads = True
        # Stop thread for all client
        for t in self.threads:
            t.join()
        logging.debug('All reciever threads are dead')    
        c.close()
        # exit.quit(player_ID)
    #except:
        #c.close()
        #exit.quit(player_ID)    
        stop_threads = False    
        recv_thread = Thread(target=self.threaded_recieve, args=(c,lambda: stop_threads,))
        recv_thread.start()
        self.threads.append(recv_thread)
        self.word_gen()
        stop_threads = True
        for t in self.threads:
            t.join()
        self.logger.debug('All reciever threads are dead')    
        c.close()    

    def start(self, client_n:int=10):
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
        self.listening = True
        self.logger.info("socket is listening")
        thread = Thread(target = self.match_request_check,)
        thread.start()
        #start_new_thread(self.match_request_check(),)
        while True:
            try:
                self.c, self.addr = sock.accept() #accept connection from a client
            except:
                break
            self.connections.append(self.c)
            self.addresses.append(self.addr)

            new_client = json.loads(self.c.recv(2048).decode()) # receive name from client
            #logging.debug(new_client) # {'newClient': 'Alice'}
            #logging.debug(type(new_client)) # dict
            #logging.debug(new_client['newClient']) # Alice
            print("") 
            #print(self.connections)
            #print(self.addresses) 
            self.logger.debug("Connection from: "+str(self.addr))
            start_new_thread(self.multi_threaded_client,(self.c, new_client['newClient'])) #use current self.c to start a new thread
            self.thread_count += 1
            logging.debug(f"Thread: {self.thread_count}") 
            self.logger.debug(f"Thread: {self.thread_count}")
            #logging.debug(f"connections[] length: " + str(len(self.connections))) 
            print("")
        self.logger.info("socket is closed")
        self.listening = False
        sock.close()
    
if __name__ == '__main__':
    s = Server(6969)
    s.start(10)
