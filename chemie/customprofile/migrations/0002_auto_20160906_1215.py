# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-06 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='relationship_status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Singel'), (2, 'Opptatt'), (5, 'Hemmelig!')], default=1, verbose_name='Samlivsstatus'),
        ),
    ]
