import logging

class Getlog():
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)
            ftm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] %(message)s"
            fm = logging.Formatter(ftm)
            tf = logging.handlers.TimedRotatingFileHandler(
                filename='test.log',
                when='H',
                backupCount=3,
                encoding='utf8'
            )
            tf.setFormatter(fm)
            tf.setLevel(logging.INFO)
            cls.logger.addHandler(tf)
            conslon = cls.logger.addHandler(tf)
        return cls.logger

if __name__ == '__main__':
    logger = Getlog().get_logger()
    logger.info('hhh')