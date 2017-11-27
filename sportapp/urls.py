#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views
from datetime import datetime
dnow = datetime.now()

urlpatterns = [
    url(r'^$', views.list_view, {'year': dnow.year}, name='list_index'),
    url(r'^detail/(?P<tourney_id>[0-9]+)/edit', views.edit, name='edit'),
    url(r'^detail/(?P<tourney_id>[0-9]+)/del', views.delete, name='delete'),
    url(r'^detail/(?P<tourney_id>[0-9]+)', views.detail, name='detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/edit', views.list_edit, name='list_edit_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})', views.list_view, name='list_month'),
    url(r'^(?P<year>\d{4})/w(?P<week>\d{1,2})/edit', views.list_edit, name='list_edit_week'),
    url(r'^(?P<year>\d{4})/w(?P<week>\d{1,2})', views.list_view, name='list_week'),
    url(r'^(?P<year>\d{4})', views.list_view, name='list_year'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^upload2018/$', views.upload2018, name='upload2018'),
    url(r'^import2018/$', views.import2018, name='import2018'),
    #url(r'^importnext/$', views.importnext, name='importnext'),
    url(r'^sports/(?P<id>[0-9]+)/$', views.sport_detail, name='sport_detail'),
    url(r'^sports/(?P<sport>[0-9]+)/(?P<year>\d{4})/(?P<month>\d{2})/edit$', views.list_edit, name='sport_detail_month_edit'),
    url(r'^sports/(?P<sport>[0-9]+)/(?P<year>\d{4})/(?P<month>\d{2})/$', views.list_view, name='sport_detail_month'),
    url(r'^sports/(?P<sport>[0-9]+)/(?P<year>\d{4})/edit$', views.list_edit, name='sport_detail_year_edit'),
    url(r'^sports/(?P<sport>[0-9]+)/(?P<year>\d{4})/$', views.list_view, name='sport_detail_year'),
    url(r'^sports/$', views.sport_list, name='sport_list'),
    url(r'^loc/$', views.sport_loc, name='sport_loc'),
    url(r'^loc/(?P<id>[0-9]+)/$', views.sport_loc_detail, name='sportloc'),
    url(r'^loc/(?P<id>[0-9]+)/edit/$', views.sport_loc_detail_edit, name='sport_loc_edit'),
    url(r'^filter/$', views.list_view, {'year': dnow.year, 'month': dnow.month}, name='filter'),
    url(r'^sport_list', views.sport_list, name='sport_list'),
]
