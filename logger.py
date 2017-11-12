import logging

def get_logger(name='root'):
    logger = logging.getLogger(name)
    if not logger.handlers:
        # Only handler is being defined.
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s %(module)s %(thread)s %(levelname)s: %(message)s")
        logger.addHandler(logging.StreamHandler())
        logger.handlers[0].setFormatter(formatter)
        logger.debug('Init logger: {}'.format(name))
    return logger


def test():
    logger1 = get_logger()
    logger2 = get_logger()
    logger1.debug('Logger 1 message')
    logger2.debug('Logger 2 message')

if __name__ == '__main__':
    test()