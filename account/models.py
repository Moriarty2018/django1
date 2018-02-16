from __future__ import unicode_literals

from django.db import models

class AccountInfo(models.Model):
    acid = models.CharField(max_length=20,primary_key=True)
    user = models.ForeignKey('my_user.UserInfo')
    acdate = models.DateTimeField(auto_now=True)
    acIsPay = models.BooleanField(default=False)
    actotle = models.DecimalField(max_digits=6,decimal_places=2)
    acaddres = models.CharField(max_length=100,default='')

class AccountDetailInfo(models.Model):
    goods = models.ForeignKey('my_goods.Goods')
    account = models.ForeignKey(AccountInfo)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    count = models.IntegerField()


