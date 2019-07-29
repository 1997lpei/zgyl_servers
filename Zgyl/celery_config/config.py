from __future__ import absolute_import
from datetime import timedelta

# 配置redis作为消息队列
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
BROKER_URL = 'redis://127.0.0.1:6379/2'

# #Broker连接量
# BROKER_POOL_LIMIT = 100
# # 任务最大缓存量
# RESULT_CACHE_MAX = 1000
# #过期时间
# RESULT_EXPIRES = 3600







# #定时任务（Scheduler实现）
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/3'
# BROKER_URL = 'redis://127.0.0.1:6379/4'
#
# #指定时区
# CELERY_TIMEZONE = 'Asia/Shanghai'
#
# CELERYBEAT_SCHEDULE = {
#     'add-every-15-second': {
#         'task':'celery_config.tasks.add',
#         'schedule': timedelta(seconds=15),
#         'args': (2,5)
#     }
# }



