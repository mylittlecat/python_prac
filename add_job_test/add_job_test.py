import logging
logging.basicConfig()

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime,timedelta
from time import sleep, time
import traceback


def my_job():
        #print 'hello world!'
        #print datetime.now()
        sleep(3)
 
try:
    print "------"
    sched = BackgroundScheduler() # 如果这里的函数是BlockingScheduler(),在start()语句之后这个程序的接下来语句是不会执行的，这种情况需要先添加作业再调用start()函数
    sched.start()
    print 0000
    for i in range(10):
        #t1 = time()
        time_now=datetime.now()
        for j in range(10000):
            sched.add_job(my_job,trigger='date',run_date=time_now+timedelta(seconds=40+i*40+3*j))
        print datetime.now()-time_now # 测试添加一万条作业所需时间,参考这个数据来设置合理的作业调度时刻
        sleep(3)
        #print time()-t1
    while True:
        sleep(100)        
except:
    print traceback.format_exc()
