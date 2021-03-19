import logging
import logging.handlers
import os

class Logger():
    logger = None
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cur_path = os.path.abspath(__file__)
            data_path = os.path.join(os.path.dirname(cur_path)+os.path.sep+'../tools','log.txt')
            # 日志器
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)
            # 格式器
            ftm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] %(message)s"
            fom = logging.Formatter(ftm)
            # 处理器
            tf = logging.handlers.TimedRotatingFileHandler(
                filename= data_path,
                when='H',
                backupCount=3,
                encoding='utf8'
            )
            tf.setFormatter(fom)
            tf.setLevel(logging.INFO)
            cls.logger.addHandler(tf)
        return cls.logger


if __name__ == '__main__':
    Logger().get_logger().info('llll')
    Logger().get_logger().info('python')
    Logger().get_logger().info('jhhh')

