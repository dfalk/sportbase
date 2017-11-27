# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-15 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0007_location_typer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['-typer', 'title'], 'verbose_name': '\u041c\u0435\u0441\u0442\u043e', 'verbose_name_plural': '\u041c\u0435\u0441\u0442\u0430'},
        ),
        migrations.AddField(
            model_name='tourney',
            name='grp',
            field=models.CharField(choices=[(b'RME', b'\xd0\xa0\xd0\xb5\xd1\x81\xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd0\xbd\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5'), (b'INV', b'\xd0\x98\xd0\xbd\xd0\xb2\xd0\xb0\xd0\xbb\xd0\xb8\xd0\xb4\xd1\x8b'), (b'KMP', b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xbb\xd0\xb5\xd0\xba\xd1\x81\xd0\xbd\xd1\x8b\xd0\xb5'), (b'RUS', b'\xd0\x92\xd1\x81\xd0\xb5\xd1\x80\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd0\xb9\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5'), (b'NO', b'\xd0\x9d\xd0\xb5 \xd1\x83\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbd\xd0\xbe')], default=b'NO', max_length=5),
        ),
    ]