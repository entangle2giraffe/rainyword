import socket
import time
import configparser
import time
import logging

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

def main():
    s = init_server()

    while True:
        # Establish connection
        c, addr = s.accept()
        #logging.DEBUG(f'Got connection from {str(addr)}')
        # Send a text to the client
        c.sendall(f'Hi {str(addr)}'.encode())
        # [TODO] disconnect client first and then close server after
        # might do it in close_connection function
        c.close
        break

if __name__ == "__main__":
    main()