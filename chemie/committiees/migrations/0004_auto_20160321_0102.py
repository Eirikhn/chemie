# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committiees', '0003_auto_20160321_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committee',
            name='tile',
        ),
        migrations.AddField(
            model_name='committee',
            name='title',
            field=models.CharField(default='kek', max_length=100),
            preserve_default=False,
        ),
    ]
