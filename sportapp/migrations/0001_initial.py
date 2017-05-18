# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tourney',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('participants', models.IntegerField(default=10)),
                ('date_start', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0')),
                ('date_end', models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd0\xba\xd0\xbe\xd0\xbd\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('date_in', models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb7\xd0\xb0\xd0\xb5\xd0\xb7\xd0\xb4\xd0\xb0', blank=True)),
                ('date_out', models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x82\xd1\x8a\xd0\xb5\xd0\xb7\xd0\xb4\xd0\xb0', blank=True)),
                ('dt_start', models.DateTimeField(null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xbe \xd1\x81\xd0\xbe\xd1\x80\xd0\xb5\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb9', blank=True)),
                ('dt_opening', models.DateTimeField(null=True, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xb8\xd0\xb5', blank=True)),
                ('dt_closing', models.DateTimeField(null=True, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xb8\xd0\xb5', blank=True)),
                ('judje_sum', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('reward_sum', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('print_sum', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('location', models.ForeignKey(to='sportapp.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fio', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='tourney',
            name='resp_gov',
            field=models.ForeignKey(related_name='worker_gov', blank=True, to='sportapp.Worker', null=True),
        ),
        migrations.AddField(
            model_name='tourney',
            name='resp_uso',
            field=models.ForeignKey(related_name='worker_uso', blank=True, to='sportapp.Worker', null=True),
        ),
        migrations.AddField(
            model_name='tourney',
            name='resp_zam',
            field=models.ForeignKey(related_name='worker_zam', blank=True, to='sportapp.Worker', null=True),
        ),
        migrations.AddField(
            model_name='tourney',
            name='sport',
            field=models.ForeignKey(to='sportapp.Sport'),
        ),
    ]
