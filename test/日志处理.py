import logging
import logging.handlers
# 日志器
logger = logging.getLogger()

logger.setLevel(logging.INFO)
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
logger.addHandler(tf)

if __name__ == '__main__':
    logger.debug('hello')
    logger.info('python')