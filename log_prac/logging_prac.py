import logging

logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
datefmt='%a, %d %b %Y %H:%M:%S',
filename='myapp.log',
filemode='a' # 参数可以是a或者w,w会清空文件再写入
)

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

