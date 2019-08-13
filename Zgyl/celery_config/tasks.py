import time
from celery_config.celery import celery_app

@celery_app.task
def add(x,y):

    time.sleep(5)
    print('1111111')
    return x + y

@celery_app.task
def add1(x,y):
    print('22222')
    return x + y

