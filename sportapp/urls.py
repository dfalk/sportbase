#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views
from datetime import datetime
dnow = datetime.now()

urlpatterns = [
    url(r'^$', views.list_view, {'year': dnow.year}, name='list_index'),
    url(r'^detail/(?P<tourney_id>[0-9]+)/edit', views.edit, name='edit'),
    url(r'^detail/(?P<tourney_id>[0-9]+)', views.detail, name='detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/edit', views.list_edit, name='list_edit_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})', views.list_view, name='list_month'),
    url(r'^(?P<year>\d{4})/w(?P<week>\d{2})/edit', views.list_edit, name='list_edit_week'),
    url(r'^(?P<year>\d{4})/w(?P<week>\d{2})', views.list_view, name='list_week'),
    url(r'^(?P<year>\d{4})', views.list_view, name='list_year'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^sports/(?P<id>[0-9]+)/$', views.sport_detail, name='sport_detail'),
    url(r'^sports/$', views.sport_list, name='sport_list'),
    #url(r'^month_gov/$', views.month_gov, name='month_gov'),
    #url(r'^edit/$', views.edit, name='edit'),
]
