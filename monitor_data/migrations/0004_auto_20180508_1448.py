# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-08 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_data', '0003_auto_20180504_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionoperation',
            name='msg_format',
            field=models.TextField(default='主机:{hostname}\n    IP:{ip}\n    应用集:{name},存在问题\n    内容:{msg}\n    ', verbose_name='消息格式'),
        ),
    ]
