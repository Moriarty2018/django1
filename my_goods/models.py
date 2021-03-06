from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    title = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.title.encode('utf-8')

class Goods(models.Model):
    gtitle = models.CharField(max_length=30)
    gpic = models.ImageField(upload_to='goods')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20,default='500g')
    gclick = models.IntegerField(default=0)
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()
    gcontent = HTMLField()
    gtype = models.ForeignKey(TypeInfo)
    def __str__(self):
        return self.gtitle.encode('utf-8')