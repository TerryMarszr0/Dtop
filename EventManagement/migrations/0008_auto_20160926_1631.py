# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-26 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagement', '0007_auto_20160926_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='edit_time',
        ),
        migrations.AddField(
            model_name='items',
            name='finish_time',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u4e8b\u9879\u7ed3\u675f\u65f6\u95f4'),
        ),
    ]
