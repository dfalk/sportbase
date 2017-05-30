# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': '\u041c\u0435\u0441\u0442\u043e', 'verbose_name_plural': '\u041c\u0435\u0441\u0442\u0430'},
        ),
        migrations.AlterModelOptions(
            name='sport',
            options={'verbose_name': '\u0421\u043f\u043e\u0440\u0442', 'verbose_name_plural': '\u0421\u043f\u043e\u0440\u0442'},
        ),
        migrations.AlterModelOptions(
            name='tourney',
            options={'verbose_name': '\u0421\u043e\u0440\u0435\u0432\u043d\u043e\u0432\u0430\u043d\u0438\u0435', 'verbose_name_plural': '\u0421\u043e\u0440\u0435\u0432\u043d\u043e\u0432\u0430\u043d\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name': '\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a', 'verbose_name_plural': '\u0420\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0438'},
        ),
        migrations.AddField(
            model_name='tourney',
            name='closing_by_end',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xbe \xd0\xbe\xd0\xba\xd0\xbe\xd0\xbd\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8e'),
        ),
        migrations.AddField(
            model_name='tourney',
            name='resp_org',
            field=models.CharField(default=b'\xd0\x9c\xd0\xb8\xd0\xbd\xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82', max_length=250, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb2. \xd0\xbe\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f'),
        ),
        migrations.AddField(
            model_name='tourney',
            name='time_text',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tourney',
            name='time_vfd',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='judje_sum',
            field=models.DecimalField(default=0, verbose_name=b'\xd0\xa1\xd1\x83\xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd0\xba\xd0\xb8\xd0\xb5', max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='location',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x81\xd1\x82\xd0\xb0', to='sportapp.Location'),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='participants',
            field=models.IntegerField(default=10, verbose_name=b'\xd0\xa3\xd1\x87\xd0\xb0\xd1\x81\xd1\x82\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='print_sum',
            field=models.DecimalField(default=0, verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x87\xd0\xb0\xd1\x82\xd0\xbd\xd0\xb0\xd1\x8f', max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='resp_gov',
            field=models.ForeignKey(related_name='worker_gov', verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb2. \xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2-\xd0\xb2\xd0\xbe', blank=True, to='sportapp.Worker', null=True),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='resp_uso',
            field=models.ForeignKey(related_name='worker_uso', verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb2. \xd0\xa3\xd0\xa1\xd0\x9e', blank=True, to='sportapp.Worker', null=True),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='resp_zam',
            field=models.ForeignKey(related_name='worker_zam', verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb2. \xd0\xb7\xd0\xb0\xd0\xbc', blank=True, to='sportapp.Worker', null=True),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='reward_sum',
            field=models.DecimalField(default=0, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb3\xd1\x80\xd0\xb0\xd0\xb4\xd0\xbd\xd0\xb0\xd1\x8f', max_digits=15, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='sport',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82', to='sportapp.Sport'),
        ),
        migrations.AlterField(
            model_name='tourney',
            name='title',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
    ]
