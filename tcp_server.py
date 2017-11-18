from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print(self.__class__.__name__)
        print('Received connection request from {0}'.format(self.client_address))
        while True:
            msg = self.request.recv(4096)
            if not msg:
                print('Connection closed by peer side')
                break
            # echo server - reply with recv msg
            self.request.send(msg)
            print('Received & send msg: {0}'.format(msg.decode(encoding='UTF-8').rstrip()))


class EchoHandler2(BaseRequestHandler):
    def handle(self):
        print(self.__class__.__name__)
        print('Received connection request from {0}'.format(self.client_address))
        for msg in iter(lambda: self.request.recv(4096), 'Exit\n'.encode('ascii')):
            #if 'Exit' received then close connection
            if not msg:
                print('Connection closed by peer side')
                break
            # echo server - reply with recv msg
            self.request.send(msg)
            print('Received & send msg: {0}'.format(msg.decode(encoding='UTF-8').rstrip()))
        else:
            print('\'Exit\\n\' msg received - closing connection.')

class EchoHandler3(StreamRequestHandler):
    def handle(self):
        print(self.__class__.__name__)
        print('Received connection request from {0}'.format(self.client_address))
        # self.rfile is similar to file object for reading
        for line in self.rfile:
            # need to receive new line sign, otherwise is blocked
            # self.wfile is similar to file object for writing
            print('Received & send msg: {0}'.format(line.decode(encoding='UTF-8').rstrip()))
            self.wfile.write(line)



class TcpServer():
    def __init__(self, handler = EchoHandler2, port = 9999):
        self.server = TCPServer(('', port), handler)
        print('TCP server started.')
        self.run_forever()

    def run_forever(self):
        # Could start it in separate thread
        self.server.serve_forever()

if __name__ == '__main__':
    TcpServer()

