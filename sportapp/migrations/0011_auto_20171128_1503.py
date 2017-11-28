# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0010_auto_20171128_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourney',
            name='ambulance_sum',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name=b'\xd0\xa1\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x8f \xd0\xbf\xd0\xbe\xd0\xbc\xd0\xbe\xd1\x89\xd1\x8c( \xd1\x81\xd1\x83\xd0\xbc\xd0\xbc\xd0\xb0 )'),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='ambulance_time',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name=b'\xd0\xa1\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x8f \xd0\xbf\xd0\xbe\xd0\xbc\xd0\xbe\xd1\x89\xd1\x8c( \xd1\x87\xd0\xb0\xd1\x81\xd1\x8b )'),
        ),
    ]