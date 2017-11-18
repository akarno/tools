from socket import socket, AF_INET, SOCK_STREAM


class TcpClient():
    def __init__(self, port = 9999):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(('localhost', port))


def send_recv_msg(s, msg):
    print('Sending msg: {}'.format(msg.rstrip()))
    s.send(msg.encode('ascii'))
    s.recv(4096)
    print('Received msg: {}'.format(msg.rstrip()))

def test_exit(s):
    send_recv_msg(s, 'Hello\n')
    send_recv_msg(s, 'Exit\n')

def test_hello(s):
    send_recv_msg(s, 'Hello\n')


if __name__ == '__main__':

    tcp_client = TcpClient()
    test_hello(tcp_client.socket)

    tcp_client2 = TcpClient()
    test_exit(tcp_client.socket)