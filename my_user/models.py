from __future__ import unicode_literals

from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=30)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    ushouname = models.CharField(max_length=30,default='')
    uaddres = models.CharField(max_length=100,default='')
    uyoubian = models.CharField(max_length=6,default='')
    uphone = models.CharField(max_length=11,default='')