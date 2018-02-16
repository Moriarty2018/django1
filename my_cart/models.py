#coding+utf-8
from __future__ import unicode_literals

from django.db import models

class CartInfo(models.Model):
    user = models.ForeignKey('my_user.UserInfo')
    goods = models.ForeignKey('my_goods.Goods')
    count = models.IntegerField()

