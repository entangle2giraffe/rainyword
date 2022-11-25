import socket
import json
import time

def client_program():
        host = socket.gethostname()
        port = 6969
        new_Client= {"newClient":"Bob"} # client's entered nickname

        client_socket = socket.socket()
        client_socket.connect((host, port)) # connect to the server
        client_socket.send(json.dumps(new_Client).encode()) # send nickname to the server
        data = client_socket.recv(1024).decode() # recieve assignID from server
        print(data)
        assigned_id = json.loads(data)['assignID']

        '''
        # simulate a client request for player_list every 3 seconds
        while True: 
                client_socket.send(json.dumps({"requestPlayerList":assigned_id}).encode()) # request player_list from the server
                data = client_socket.recv(1024).decode()
                print(data)
                time.sleep(3)
        '''

        message = input(" -> ") # take input
        while message.lower().strip() != 'bye': # when send bye to server the connection is close
                client_socket.send(message.encode())                      
                data = client_socket.recv(1024).decode() 
                print('Recieved from server: ' + data)   
                message = input(" -> ")
        client_socket.close()


if __name__ == "__main__":
        client_program()
                            