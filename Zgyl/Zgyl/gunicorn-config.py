# -*- coding: utf-8 -*-
import os
# import sys
# import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elevator_temp.settings')
# django.setup()
from multiprocessing import cpu_count

# import my_config

# sys.path.insert(0, '../')
bind = ["127.0.0.1:8004"]
daemon = False

# pidfile = os.path.join(my_config.LOG_DIR, 'gunicorn.pid')

# chdir = "/home/lpei/桌面/Zgyl"
workers = cpu_count()  # 工作进程数量
worker_class = "gevent"  # 指定一个异步处理的库
worker_connections = 65535

keepalive = 60
timeout = 30
graceful_timeout = 10
forwarded_allow_ips = '*'

# 日志处理
capture_output = True
loglevel = 'debug'
errorlog = os.path.join('/home/lpei/桌面/Zgyl/static/logs', 'error.log')



# gunicorn -c  project_name/gunicorn-api.py project_name.wsgi
# gunicorn -c  Zgyl/gunicorn-api.py  Zgyl.wsgi

# gunicorn Zgyl.wsgi:application -b 127.0.0.1:8004