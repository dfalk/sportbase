#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import modelformset_factory
from django.db import models
from django.forms import ModelForm
from .models import Tourney

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
        fields=('title', 'sport', 'location', 'participants', 'date_start', 'date_end', 'date_in', 'date_out', 'time_text', 'time_vfd', 'resp_org', 'resp_gov', 'resp_zam', 'resp_uso')
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
    file_name = forms.FileField(label='Файл', max_length=100)

class LocForm(ModelForm):
        class Meta:
           model = Tourney
           fields = ['location','title']

class FilterForm(forms.Form):
      date_start = forms.DateField(label="Начало")
      date_end = forms.DateField(label="Конец")
