# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-26 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagement', '0002_auto_20160926_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='items_content',
            field=models.TextField(max_length=128, verbose_name='\u4e8b\u9879\u8bf4\u660e'),
        ),
    ]
