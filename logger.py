import logging

def setup_custom_logger(name='root'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(module)s %(thread)s %(levelname)s: %(message)s")
    logger.addHandler(logging.StreamHandler())
    logger.handlers[0].setFormatter(formatter)
    logger.debug('Init logger: {}'.format(name))
    return logger


if __name__ == '__main__':
    setup_custom_logger()