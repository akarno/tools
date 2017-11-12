# server.py
import select
import socket
import time
import threading

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
            client_thread = threading.Thread(target=self.client_manager, args=[clientsocket, addr, self.logger])
            client_thread.start()

    @staticmethod
    def get_msg():
        currentTime = time.ctime(time.time())
        msg = 'Server msg: {0}'.format(currentTime)
        return msg

    def client_manager(self, client_socket, addr, logger):

        SELECT_TIMEOUT_SECONDS = 2
        PING_TIMEOUT_SECONDS = 1
        CONNECTION_TIMEOUT_SECONDS = 5
        last_ping_time = time.time()
        start_time = last_ping_time
        while True:
            current_time = time.time()

            if current_time - start_time > CONNECTION_TIMEOUT_SECONDS - 1:
                #TODO to trzeba wyniesc na zewnatrz
                (rlist, wlist, xlist) = select.select([], [client_socket], [], SELECT_TIMEOUT_SECONDS)
                if len(wlist) > 0:
                    msg = 'Exit'
                    client_socket.send(msg.encode('ascii'))
                    logger.debug('Sending message (addr: {0}): {1}'.format(addr, msg))
                    break

            if current_time - last_ping_time > PING_TIMEOUT_SECONDS:
                last_ping_time = current_time
                (rlist, wlist, xlist) = select.select([], [client_socket], [], SELECT_TIMEOUT_SECONDS)
                if len(wlist) > 0:
                    msg = SocketServer.get_msg()
                    client_socket.send(msg.encode('ascii'))
                    logger.debug('Sending message (addr: {0}): {1}'.format(addr, msg))


            if current_time - start_time > CONNECTION_TIMEOUT_SECONDS:
                break

            #TODO teraz zrobic zamykanie serwera od strony clienta - jak przyjdzie exit - to polaczenie zamkniete od clienta
            #lacznie 4 mozliwe zamkniecia - obie strony przez wyslanie exit, obie strony przez zamkniecie polaczenia


        client_socket.close()
        self.logger.debug('Connection {0}/{1} closed.'.format(client_socket, addr))
        #zrobic tutaj wysylanie wiadomosci losowo tak dlugo az nie otrzymamy z clienta prosby o zamkniecie polaczenia


if __name__ == '__main__':
    socket_server = SocketServer()
    socket_server.run_server()

