# import time,datetime
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# def func():
#     now = datetime.datetime.now()
#     ts = now.strftime('%Y-%m-%d %H:%M:%S')
#     print('do func time:',ts)
#
# def dojob():
#     #创建调度器
#     scheduler = BlockingScheduler()
#     #添加任务,间隔2秒
#     scheduler.add_job(func,'interval',minutes=30,start_date='2019-08-01 24:00:00' ,
#                       end_date='2019-12-31 24:00:00')
#     scheduler.start()
#
# dojob()

from celery_config.tasks import add,add1

def have():
    print(add.delay(2,4))
    print(add1.delay(3,5))

have()