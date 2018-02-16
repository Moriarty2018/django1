# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-27 05:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_goods', '0002_auto_20180127_1351'),
        ('my_user', '0002_auto_20180125_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_goods.Goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_user.UserInfo')),
            ],
        ),
    ]