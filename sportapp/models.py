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
    loc_choices = (('USS','УСС'),
	      ('RME','Район'),
              ('RU','Другой регион'),
              ('NO','Не установлено'))
    typer = models.CharField(choices=loc_choices, max_length=5, default='NO')
    
    class Meta:
        ordering = ['-typer','title']
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
    location2 = models.ForeignKey(Location, verbose_name='Место2', related_name='tourneys2',
        null=True, blank=True)
    location3 = models.ForeignKey(Location, verbose_name='Место3', related_name='tourneys3',
        null=True, blank=True)
    location4 = models.ForeignKey(Location, verbose_name='Место4', related_name='tourneys4',
        null=True, blank=True)
    is_uss = models.BooleanField('На базе УСС', default=True)
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
    pitanie_sum = models.DecimalField('Питание', max_digits=15, decimal_places=2, default=0)
    projiv_sum = models.DecimalField('Проживание', max_digits=15, decimal_places=2, default=0)
    proezd_sum = models.DecimalField('Проезд (билеты)', max_digits=15, decimal_places=2, default=0)
    vznos_sum = models.DecimalField('Заявочный взнос', max_digits=15, decimal_places=2, default=0)
    arenda_sum = models.DecimalField('Аренда', max_digits=15, decimal_places=2, default=0)
    medic_sum = models.DecimalField('Медики', max_digits=15, decimal_places=2, default=0)
    transport_sum = models.DecimalField('Транспорт', max_digits=15, decimal_places=2, default=0)
    bus_on = models.BooleanField('Фрахтование автобуса', default=False)
    cup1_sum = models.DecimalField('Сумма кубков за 1 место', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    cup1_kol = models.IntegerField('Кол-во кубков за 1 место', blank=True, null=True, default=0)
    cup2_sum = models.DecimalField('Сумма кубков за 2 место', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    cup2_kol = models.IntegerField('Кол-во кубков за 2 место', blank=True, null=True, default=0)
    cup3_sum = models.DecimalField('Сумма кубков за 3 место', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    cup3_kol = models.IntegerField('Кол-во кубков за 3 место', blank=True, null=True, default=0)
    cups_sum = models.DecimalField('Сумма кубков', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    cups_kol = models.IntegerField('Кол-во кубков', blank=True, null=True, default=0)
    tokens_sum = models.DecimalField('Сумма жетонов', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    tokens_kol = models.IntegerField('Кол-во жетонов', blank=True, null=True, default=0)
    medals_sum = models.DecimalField('Сумма медалей', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    medals_kol = models.IntegerField('Кол-во медалей', blank=True, null=True, default=0)
    prizes_sum = models.DecimalField('Сумма призов', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    prizes_kol = models.IntegerField('Кол-во призов', blank=True, null=True, default=0)
    diploms_sum = models.DecimalField('Сумма дипломов', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    diploms_kol = models.IntegerField('Кол-во дипломов', blank=True, null=True, default=0)
    postersA4_sum = models.DecimalField('Сумма афиш А4', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    postersA4_kol = models.IntegerField('Кол-во афиш А4', blank=True, null=True, default=0)
    postersA3_sum = models.DecimalField('Сумма афиш А3', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    postersA3_kol = models.IntegerField('Кол-во афиш А3', blank=True, null=True, default=0)
    postersA2_sum = models.DecimalField('Сумма афиш А2', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    postersA2_kol = models.IntegerField('Кол-во афиш А2', blank=True, null=True, default=0)
    banners_sum = models.DecimalField('Сумма баннеров', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    banners_kol = models.IntegerField('Кол-во баннеров',  blank=True, null=True, default=0)
    frames_sum = models.DecimalField('Сумма рамок', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    frames_kol = models.IntegerField('Кол-во рамок', blank=True, null=True, default=0)
    badges_sum = models.DecimalField('Сумма бейджей', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    badges_kol = models.IntegerField('Кол-во бейджей', blank=True, null=True, default=0)
    stickers_sum = models.DecimalField('Сумма наклеек', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    stickers_kol = models.IntegerField('Кол-во наклеек', blank=True, null=True, default=0)
    numbers_sum = models.DecimalField('Сумма номеров', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    numbers_kol = models.IntegerField('Кол-во номеров', blank=True, null=True, default=0)
    tablesA1_sum = models.DecimalField('Сумма таблиц А1', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    tablesA1_kol = models.IntegerField('Кол-во таблиц А1', blank=True, null=True, default=0)
    ambulance_time = models.DecimalField('Скорая помощь( часы )', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    ambulance_sum = models.DecimalField('Скорая помощь( сумма )', max_digits=5, blank=True, null=True, decimal_places=2, default=0)
    report = models.BooleanField('Отчет', blank=True, default=0)
    protocol = models.BooleanField('Протокол', blank=True, default=0)
    resp_org = models.CharField(default='Минспорт', max_length=250,
        verbose_name='Отв. организация')
    resp_gov = models.ForeignKey(Worker, null=True, blank=True,
        related_name="worker_gov", verbose_name='Отв. прав-во')
    resp_zam = models.ForeignKey(Worker, null=True, blank=True,
        related_name="worker_zam", verbose_name='Отв. зам')
    resp_uso = models.ForeignKey(Worker, null=True, blank=True,
        related_name="worker_uso", verbose_name='Отв. УСО')
    choice = (('1','Минспорт'), 
	      ('2','Выезд'), 
              ('3','Другое')) 
    typer = models.CharField(choices=choice, max_length=25, default=1)
    grp_choice = (('RME','Республиканские'), 
	      ('INV','Инвалиды'), 
              ('KMP','Комплексные'),
              ('RUS','Всероссийские'),
              ('NO','Не указано')) 
    grp = models.CharField(choices=grp_choice, max_length=5, default='NO')
	
	

    class Meta:
        ordering = ['date_start']
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"

    def __unicode__(self):
        return self.title
