# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-13 07:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_data', '0016_auto_20180613_1414'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'permissions': (('can_show_application', '可访问应用集页面'), ('can_show_add_application', '可访问创建应用集页面'), ('can_add_application', '可创建应用集'), ('can_del_application', '可删除应用集'), ('can_show_edit_application', '可访问编辑应用集页面'), ('can_edit_application', '可编辑应用集')), 'verbose_name_plural': '应用集表'},
        ),
        migrations.AlterModelOptions(
            name='hostgroup',
            options={'permissions': (('can_show_host_group', '可访问主机组页面'), ('can_show_add_host_group', '可访问创建主机组页面'), ('can_add_host_group', '可创建主机组'), ('can_del_host_group', '可删除主机组'), ('can_show_edit_host_group', '可访问编辑主机组页面'), ('can_edit_host_group', '可编辑主机组')), 'verbose_name_plural': '主机组表'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'permissions': (('can_show_item', '可访问监控项页面'), ('can_show_add_item', '可访问创建监控项页面'), ('can_add_item', '可创建监控项'), ('can_del_item', '可删除监控项'), ('can_show_edit_item', '可访问编辑监控项页面'), ('can_edit_item', '可编辑监控项')), 'verbose_name_plural': '监控项表'},
        ),
    ]
