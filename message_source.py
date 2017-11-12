
import time
import threading
import queue
import enum
from random import randrange
from logger import get_logger

class Messages(enum.Enum):
    EXIT = enum.auto()

class MessageSource():

    def __init__(self, stop_event = None, consumer = None):
        self.logger = get_logger()
        if not consumer:
            consumer = self.logger.debug
        if not stop_event:
            stop_event = threading.Event()
        self.stop_event = stop_event
        self.logger.debug('Starting new message server with consumer: {0}'.format(consumer))
        self.msg_thread = threading.Thread(target=self.message_manger, args=[stop_event, consumer])
        self.start()

    def start(self):
        self.msg_thread.start()

    def stop(self):
        self.stop_event.set()
        self.logger.debug('Stopping message streaming.')
        self.msg_thread.join()
        self.logger.debug('Stopped message streaming thread.')

    @staticmethod
    def get_message():
        current_time = time.time()
        msg = '{0}'.format(time.ctime(current_time))
        return msg

    def message_manger(self, stop_event, consumer):

        while True:
            if stop_event.is_set():
                msg = Messages.EXIT
                consumer(msg)
                break
            msg = MessageSource.get_message()
            consumer(msg)
            time.sleep(randrange(1,4))


def test_logger():
    msg_src = MessageSource()
    time.sleep(10)
    msg_src.stop()

def test_queue():
    msg_queue = queue.Queue()
    msg_src = MessageSource(consumer=msg_queue.put)
    n = 0
    while True:
        msg = msg_queue.get()
        msg_src.logger.debug(msg)
        if msg == Messages.EXIT:
            break
        n+=1
        if n > 4:
            msg_src.stop()

if __name__ == '__main__':
    test_logger()
    test_queue()
    test_queue()