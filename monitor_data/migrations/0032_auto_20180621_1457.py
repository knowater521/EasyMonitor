# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-21 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_data', '0031_auto_20180620_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号'),
        ),
    ]