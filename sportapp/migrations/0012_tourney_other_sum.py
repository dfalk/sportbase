# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0011_auto_20171128_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='other_sum',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd1\x87\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb0\xd1\x81\xd1\x85\xd0\xbe\xd0\xb4\xd1\x8b'),
        ),
    ]
