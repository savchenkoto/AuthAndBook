# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0004_auto_20171114_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(default='Fill that later'),
        ),
    ]
