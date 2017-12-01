#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import modelformset_factory, formset_factory
from django.db import models
from django.forms import ModelForm
from .models import Tourney, Sport, Location

class TourneyForm(forms.ModelForm):

    #sport_display = forms.CharField(max_length=100, help_text='type')
    #loc_display = forms.CharField(max_length=100, help_text='type')

    class Meta:
        model = Tourney
        exclude = ('dt_start',)
        #fields=('title', 'sport', 'location', 'participants', 'date_start', 'date_end', 'date_in', 'date_out', 'time_text', 'time_vfd', 'resp_org', 'resp_gov', 'resp_zam', 'resp_uso')
        widgets={
            'title': forms.Textarea(attrs={}),
            }

class TourneyMassForm(forms.ModelForm):

    #sport_display = forms.CharField(max_length=100, help_text='type')
    #loc_display = forms.CharField(max_length=100, help_text='type')

    class Meta:
        model = Tourney
        fields=('title', 'sport', 'location', 'location2', 'location3', 'location4', 'participants', 'date_start', 'date_end', 'date_in', 'date_out', 'time_text', 'time_vfd', 'resp_org', 'resp_gov', 'resp_zam', 'resp_uso', 'judje_sum', 'reward_sum', 'print_sum', 'typer', 'grp', 'cup1_sum', 'cup1_kol', 'cup2_sum', 'cup2_kol', 'cup3_sum', 'cup3_kol', 'cups_sum', 'cups_kol', 'tokens_sum', 'tokens_kol', 'medals_sum', 'medals_kol', 'prizes_sum', 'prizes_kol', 'diploms_sum', 'diploms_kol', 'postersA4_sum', 'postersA4_kol', 'postersA3_sum', 'postersA3_kol', 'postersA2_sum', 'postersA2_kol', 'banners_sum', 'banners_kol', 'frames_sum', 'frames_kol', 'badges_sum', 'badges_kol', 'stickers_sum', 'stickers_kol', 'numbers_sum', 'numbers_kol', 'tablesA1_sum', 'tablesA1_kol', 'ambulance_sum', 'ambulance_time', 'report', 'protocol', 'grp')
        widgets={
            'title': forms.HiddenInput(attrs={}),
            #'sport': forms.HiddenInput(attrs={}),
            #'location': forms.HiddenInput(attrs={}),
            #'resp_gov': forms.TextInput(attrs={}),
            #'resp_zam': forms.TextInput(attrs={}),
            #'resp_uso': forms.TextInput(attrs={}),
            }

TourneyFormSet = modelformset_factory(Tourney, form=TourneyMassForm, extra=0)

class UploadForm(forms.Form):
    sport = forms.ModelChoiceField(queryset=Sport.objects.all())
    location = forms.ModelChoiceField(queryset=Location.objects.all())
    file_name = forms.FileField(label='Файл', max_length=100)

class UploadFormxl(forms.Form):
    file_name = forms.FileField(label='Файл', max_length=100)

class ImportForm(forms.Form):
    title = forms.CharField(max_length=200)
    date_start = forms.DateField()
    location = forms.ModelChoiceField(queryset=Location.objects.all())

ImportFormSet = formset_factory(ImportForm, extra=0)
        
class LocForm(ModelForm):
        class Meta:
           model = Tourney
           fields = ['location','title']

class FilterForm(forms.Form):
      date_start = forms.DateField(label="Начало")
      date_end = forms.DateField(label="Конец")
      sport = forms.ModelChoiceField(queryset=Sport.objects.all(), required=False)
      choice = (('13', 'Республиканские'),
                ('1', 'Минспорт'),
                ('2', 'Выезд'),
	        ('3', 'Другое'))
      typer = forms.ChoiceField(choices=choice,label="Организация")
      only_start = forms.BooleanField(required=False, label="Только начало")
