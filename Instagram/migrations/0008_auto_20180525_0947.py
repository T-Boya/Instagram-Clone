# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-25 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0007_auto_20180524_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='likes',
        ),
        migrations.AddField(
            model_name='photo',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]