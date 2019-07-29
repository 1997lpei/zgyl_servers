from django.db import models

# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=16,unique=True)
    passWord = models.CharField(max_length=64)
    upTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'User'


class Server(models.Model):
    serverID = models.CharField(max_length=64,unique=True)
    serialNumber = models.CharField(max_length=64,unique=True)
    serverName = models.CharField(max_length=16)
    serverCore = models.CharField(max_length=64)
    status = models.BooleanField(default=0)

    class Meta:
        db_table = 'Server'