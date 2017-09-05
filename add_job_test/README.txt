add_job()函数是python任务调度模块apscheduler下面的一个用于给调度器添加作业的函数，add_job()函数的可选参数很多，详细地可以进入python交互界面通过
import apscheduler
help()
apscheduler.schedulers.background.BackgroundScheduler.add_job(或apscheduler.schedulers.blocking.BlockingScheduler.add_job)
来查看
值得注意的一点是，如果add_job()函数中trigger的参数为date，但是run_date的时间已经错过的话，作业调度会终止，这时可以在文件的开头处加入：
import logging
logging.basicConfig()
来排查错误
######################################################################################

add_job_test.py是一个用于测试add_job()函数调用次数很大时对应进程所占用内存资源的程序
