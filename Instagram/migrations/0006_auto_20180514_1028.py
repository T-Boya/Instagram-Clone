# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-14 07:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Instagram', '0005_photo_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='photo',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Instagram.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(blank=True, default='nice!', max_length=1000),
        ),
    ]
