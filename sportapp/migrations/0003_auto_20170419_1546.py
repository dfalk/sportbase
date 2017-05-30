# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0002_auto_20170419_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='position',
            field=models.CharField(default='-', max_length=100, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbb\xd0\xb6\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tourney',
            name='time_text',
            field=models.TextField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xb2\xd1\x81\xd0\xb5\xd1\x85', blank=True),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='time_vfd',
            field=models.TextField(null=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbc\xd0\xb5\xd0\xb4\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2', blank=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='fio',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa4\xd0\x98\xd0\x9e'),
        ),
    ]
