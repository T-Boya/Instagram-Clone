# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-29 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0012_auto_20180528_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='followed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
