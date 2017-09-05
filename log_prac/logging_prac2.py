#coding:utf-8
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
# 以上格式是写入filename文件中的信息的格式
datefmt='%a, %d %b %Y %H:%M:%S',
filename='/home/bijy/python_prac/log_prac/myapp.log',
filemode='a' # 参数可以是a或者w,w会清空文件再写入
)
logger = logging.getLogger('Spiderman')
logger2 = logging.getLogger('Superman')
#################################################################################################################
#定义一个StreamHandler,将INFO级别或更高的日志打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(funcName)s %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)
logger2.addHandler(console)
#################################################################################################################
#定义一个RotatingFileHandler,最多备份5个日志文件，每个日志文件最大1k
Rthandler = RotatingFileHandler('/home/bijy/python_prac/log_prac/myapp.log',maxBytes=1024,backupCount=5)
Rthandler.setLevel(logging.INFO)
Rthandler.setFormatter(formatter)
logger.addHandler(Rthandler)
logger2.addHandler(Rthandler)
#################################################################################################################
for i in range(10000):
    logger.debug('%d This is debug message' % i)
    logger.info('%d This is info message' % i)
    logger.warning('%d This is warning message' % i)

    logger2.debug('%d This is debug message' % i)
    logger2.info('%d This is info message' % i)
    logger2.warning('%d This is warning message' % i)
if logging.getLogger('Superman')==logger2:
    print "logging.getLogger('Superman')==logger2"
