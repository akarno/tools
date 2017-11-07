# server.py
import socket
import time
import logging

from logger import setup_custom_logger

class SocketServer():

    def __init__(self, port=9999):
        self.logger = setup_custom_logger()
        self.logger.debug('Init socket server')
        # create a socket object
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # get local machine name
        self.host = socket.gethostname()
        self.port = port
        self.socket.bind((self.host, self.port))
        self.logger.info('Server with host {0} binded on port {1}'.format(self.host, self.port))
        #TODO There’s actually 3 general ways in which this loop could work
        # - dispatching a thread to handle clientsocket
        self.socket.listen(5)

    def run_server(self):
        while True:
            # establish a connection
            clientsocket, addr = self.socket.accept()

            self.logger.debug('Got a connection from {0}'.format(addr))
            currentTime = time.ctime(time.time()) + '\r\n'
            clientsocket.send(currentTime.encode('ascii'))
            clientsocket.close()

if __name__ == '__main__':
    socket_server = SocketServer()
    socket_server.run_server()

