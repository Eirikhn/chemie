# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0003_auto_20160503_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='year',
            field=models.PositiveSmallIntegerField(default=2016),
            preserve_default=False,
        ),
    ]
