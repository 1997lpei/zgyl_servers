from __future__ import absolute_import
from celery import Celery

# 初始化celery
celery_app = Celery('celery_config',include=['celery_config.tasks'])
celery_app.config_from_object('celery_config.config')

#过期时间
celery_app.conf.update(
    result_expires=3600
)

if __name__ == '__main__':
    celery_app.start()



