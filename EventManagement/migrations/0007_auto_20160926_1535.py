# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-26 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagement', '0006_items_items_rete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='items_rete',
        ),
        migrations.AddField(
            model_name='items',
            name='items_rate',
            field=models.CharField(default=0, max_length=5, verbose_name='\u4e8b\u9879\u5b8c\u6210\u767e\u5206\u767e'),
        ),
    ]
