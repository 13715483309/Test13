import logging
import logging.handlers

class Getlog():
    def __init__(self):
        # 日志器
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def get_logger(self):
        # 格式器
        fmt = "%(asctime)s - %(levelname)s - [%(name)s] [%(funcName)s:%(lineno)d - %(message)s]"
        fm = logging.Formatter(fmt)
        # 处理器
        tf = logging.handlers.TimedRotatingFileHandler(
            filename = 'test.log',
            when ='H',
            backupCount = 3,
            encoding = 'utf8'
        )

        tf.setFormatter(fm)
        tf.setLevel(logging.INFO)
        self.logger.addHandler(tf)

        return self.logger

if __name__ == '__main__':
    logger = Getlog().get_logger()
    logger.debug('hello')
    logger.info('python2')