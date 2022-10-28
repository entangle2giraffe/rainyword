import socket

def client_program():
        host = socket.gethostname()
        port = 6969

        client_socket = socket.socket()
        client_socket.connect((host, port))

        message = input(" -> ") # take input
        while message.lower().strip() != 'bye': # when send bye to server the connection is close
                client_socket.send(message.encode())                      
                data = client_socket.recv(1024).decode() 
                print('Recieved from server: ' + data)   
                message = input(" -> ").lower()

        client_socket.close()


if __name__ == "__main__":
        client_program()
                            