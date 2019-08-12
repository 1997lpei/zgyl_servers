from django.db import models
from datetime import datetime

# Create your models here.
class Machine(models.Model):
    m_date = models.DateField(verbose_name='日期')
    m_time = models.TimeField(verbose_name='时间')
    traffic = models.FloatField(verbose_name='流量')
    diskname = models.CharField(max_length=128,verbose_name='云硬盘名称')

    def add_data(self,m_date,m_time,traffic,diskname):
        """
        添加数据到mysql
        :param m_date:
        :param m_time:
        :param traffic:
        :param diskname:
        :return:
        """
        m_date = datetime.strptime(m_date,'%m/%d/%Y').date()
        self.m_date = m_date
        self.m_time = m_time
        self.traffic = traffic
        self.diskname = diskname
        self.save()

    def to_dict(self):
        """
        格式化数据
        :return:
        """
        return {
            str(self.m_time): self.traffic
        }

    class Meta:
        db_table = 'Machine'
