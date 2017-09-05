这里面主要是关于logging模块的练习，其中：
#######################################################################################

logging_prac.py：
    是建立一个名为'root'的logging对象的练习，是最基本的操作；
#######################################################################################

logging_prac2.py：
    不仅创建了'root'对象，还通过logging.getLogger()创建了名为'Spiderman'和'Superman'的logging对象，在没有添加任何handler之前，它们的配置都是
    logging.basicConfig()中的配置；

    logging.StreamHandler()用于创建一个handler，它的功能是将日志打印到标准错误中，在这个handler对象上可以调用setLevel()方法设置打印日志的级别，调用setFormatter()方法来设置handler的打印格式，最后通过调用logging对象的addHandler()方法把handler添加到logging对象中，之后这个logging对象就具有handler中的设置了;

    日志的级别分为：DEBUG,INFO,WARNING,ERROR,CRITICAL,默认的日志级别是WARNING,这意味着如果没有设置日志级别，默认打印WANING及以上级别的信息；

    RotatingFileHandler('path',maxBytes=int,backupCount=int)用于产生备份日志,'path'指的是备份日志文件路径，maxBytes这个参数指的是每个备份日志文件的大小，单位是Bytes，backupCount指的是产生备份日志文件的数量，这里有一个tips，如果logging.basicConfig()中生成日志的路径和这里的'path'路径一致，就可以控制日志文件的大小每个不超过maxBytes，如果不是这样的话，logging.basicConfig()中设置的日志文件会一直增大下去，这是不可接受的，所以最好把路径设置为一致；
#######################################################################################

logger.conf:
    这是一个配置logging对象的文件，这个文件是在网上找的，写好之后通过 logging.config.fileConfig("logger.conf")来导入,可以参看log_example_01.py中的做法
#######################################################################################

log_example_01.py：
    通过导入logger.conf文件来导入logging对象的配置并使用logging对象的一个简单例子
