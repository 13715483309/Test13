import logging
import logging.handlers
import os

class Logger():

    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 文件绝对路径
            cur_path = os.path.abspath(__file__)
            data_path = os.path.join(os.path.dirname(cur_path)+os.path.sep+'../log','log.txt')
            # 日志器
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)
            # 格式器
            formatset = '%(asctime)s-%(levelname)s' \
                        '-%(levelno)s-%(name)s' \
                        ' - %(pathname)s-%(funcName)s-%(message)s'
            format = logging.Formatter(formatset)
            # 处理器
            rf_handler = logging.handlers.TimedRotatingFileHandler(
                filename=data_path,
                when='H',
                interval=1,
                backupCount=7
            )
            rf_handler.setFormatter(format)
            cls.logger.addHandler(rf_handler)
        return cls.logger

if __name__ == '__main__':
    Logger.get_logger().info('hello')
    Logger.get_logger().info('python')