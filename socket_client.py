# client.py
import select
import socket
import sys
import time
import datetime
from logger import get_logger


class SocketClient():

    def __init__(self, port=9999):
        self.logger = get_logger()
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
        self.logger.debug('Connection closed.')

    def sent_message(self):
        currentTime = time.ctime(time.time()) + '\r\n'
        self.socket.send(currentTime.encode('ascii'))

    def monitor_socket(self):
        #zrobic select
        SELECT_TIMEOUT_SECONDS = 1
        n = 0
        try:
            while(True):
                if n > 2:
                    self.logger.debug('Monitoring finished')
                    break
                (rlist, wlist, xlist) = select.select([self.socket], [], [], SELECT_TIMEOUT_SECONDS)
                if len(rlist) == 0:
                    self.logger.debug('No data...')
                    n+=1
                    continue

                data = self.socket.recv(1024*4).decode(encoding='UTF-8', errors='strict')

                if not data:
                    self.logger.debug('Connection closed by peer side.')
                    break
                if data == 'Exit':
                    self.logger.debug('Got Exit command from peer side.')
                    break
                self.logger.info('Got msg from server: \n{0}'.format(data))


        except:
            import traceback
            exc_trace = traceback.format_exc()
            exc = sys.exc_info()[1]
            self.logger.error('Exception: {0}'.format(exc))
            self.logger.debug('Exception: {0}'.format(exc_trace))


if __name__ == '__main__':
    with SocketClient() as socket_client:
        socket_client.monitor_socket()
        #tm = socket_client.socket.recv(1024)
        #socket_client.logger.debug("The time got from the server is %s" % tm.decode('ascii'))
        #socket_client.sent_message()

