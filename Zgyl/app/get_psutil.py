from __future__ import absolute_import
import psutil
from celery_config.celery import celery_app


#磁盘信息
@celery_app.task
def get_disk_info():
    disk_total = psutil.disk_usage('/')
    disk_user = disk_total.used/1024/1024/1024
    disk_free = disk_total.free/1024/1024/1024
    disk_percent = disk_total.percent
    # disk_info = "磁盘使用：%0.2fG，使用率%0.1f%%，剩余磁盘：%0.2fG" % (disk_user, disk_percent, disk_free)

    return '%.1f' % (disk_percent/100)

#cpu信息
@celery_app.task
def get_cpu_info():
    cpu = psutil.cpu_percent(interval=1)
    # cpu_info = 'CPU使用率:%i%%' % cpu
    return '%.3f' % (cpu/100)

#内存信息
@celery_app.task
def get_memory_info():
    virtual_memory = psutil.virtual_memory()
    used_memory = virtual_memory.used/1024/1024/1024
    free_memory = virtual_memory.free/1024/1024/1024
    memory_percent = virtual_memory.percent
    # memory_info = "内存使用：%0.2fG，使用率%0.1f%%，剩余内存：%0.2fG" % (used_memory, memory_percent, free_memory)
    return '%.2f' % (memory_percent/100)

