import logging
import logging.config
from datetime import datetime

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

logger.debug(' %s:This is debug message' % datetime.now())
logger.info(' %s:This is info message' % datetime.now())
logger.warning(' %s:This is warning message' % datetime.now())

