# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0005_auto_20171115_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='about',
            field=models.TextField(),
        ),
    ]
