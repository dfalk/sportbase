#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

class Sport(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = "Спорт"
        verbose_name_plural = "Спорт"

class Location(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['title']
        verbose_name = "Место"
        verbose_name_plural = "Места"
    
    def __unicode__(self):
        res = self.title + " - " + self.city
        return res

class Worker(models.Model):
    fio = models.CharField(max_length=200, verbose_name='ФИО')
    position = models.CharField(max_length=100, verbose_name='Должность')
    
    class Meta:
        ordering = ['fio']
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
	
    def __unicode__(self):
        return self.fio

class Tourney(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    sport = models.ForeignKey(Sport, verbose_name='Спорт')
    location = models.ForeignKey(Location, verbose_name='Места')
    participants = models.IntegerField('Участники', default=10)
    date_start = models.DateField('Дата начала')
    date_end = models.DateField('Дата окончания', null=True, blank=True)
    date_in = models.DateField('Дата заезда', null=True, blank=True)
    date_out = models.DateField('Дата отъезда', null=True, blank=True)
    time_text = models.TextField('Время для всех', null=True, blank=True)
    time_vfd = models.TextField('Время для медиков', null=True, blank=True)
    dt_start = models.DateTimeField('Начало соревнований', null=True, blank=True)
    dt_opening = models.DateTimeField('Открытие', null=True, blank=True)
    dt_closing = models.DateTimeField('Закрытие', null=True, blank=True)
    closing_by_end = models.BooleanField('Закрытие по окончанию', default=False)
    judje_sum = models.DecimalField('Судейские', max_digits=15, decimal_places=2, default=0)
    reward_sum = models.DecimalField('Наградная', max_digits=15, decimal_places=2, default=0)
    print_sum = models.DecimalField('Печатная', max_digits=15, decimal_places=2, default=0)
    resp_org = models.CharField(default='Минспорт', max_length=250,
        verbose_name='Отв. организация')
    resp_gov = models.ForeignKey(Worker, null=True, blank=True,
        related_name="worker_gov", verbose_name='Отв. прав-во')
    resp_zam = models.ForeignKey(Worker, null=True, blank=True,
        related_name="worker_zam", verbose_name='Отв. зам')
    resp_uso = models.ForeignKey(Worker, null=True, blank=True,
        related_name="worker_uso", verbose_name='Отв. УСО')
    
    class Meta:
        ordering = ['date_start']
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"

    def __unicode__(self):
        return self.title
