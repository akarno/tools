# client.py
import socket

from logger import setup_custom_logger

class SocketClient():

    def __init__(self, port=9999):
        self.logger = setup_custom_logger()
        self.logger.debug('Init socket client')
        # create a socket object
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # get local machine name
        self.host = socket.gethostname()
        self.port = port

    def __enter__(self):
        # connection to hostname on the port.
        self.socket.connect((self.host, self.port))
        self.logger.debug('Connected to host {0} binded on port {1}'.format(self.host, self.port))
        return self

    def __exit__(self, *args):
        self.socket.close()


if __name__ == '__main__':
    with SocketClient() as socket_client:
        tm = socket_client.socket.recv(1024)
        socket_client.logger.debug("The time got from the server is %s" % tm.decode('ascii'))

