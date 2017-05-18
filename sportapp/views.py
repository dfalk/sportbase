#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from .models import Tourney, Sport, Location
from .forms import UploadForm, TourneyFormSet, TourneyForm
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH as align
from docx.shared import Pt
from cStringIO import StringIO
from datetime import datetime
from django.utils import formats
from django.utils.formats import localize
import calendar
import json

def list_view(request, year=None, month=None, week=None):
    weeks = []
    dnow = datetime.now()
    current_week = dnow.isocalendar()[1]
    select_week = next_week = prev_week = None
    if year:
        tourney_list = Tourney.objects.filter(date_start__year=year)
    if month:
        year_int = int(year)
        month_int = int(month)
        tourney_list = tourney_list.filter(date_start__month=month)
        first_week_month = datetime(year_int, month_int, 1).isocalendar()[1]
        last_month_day = calendar.monthrange(year_int, month_int)[1]
        last_week_month = datetime(year_int, month_int, last_month_day).isocalendar()[1]
        for week1 in range(first_week_month, last_week_month+1):
            weeks.append(week1)
    if week:
        select_week = int(week)
        next_week = select_week + 1
        prev_week = select_week - 1
        tourney_list = tourney_list.filter(date_start__week=week)
    # export block
    if request.GET.get('file', '') == 'gov':
        file_name = "sportapp/templates/sportapp/02-gov_week.docx"
        #file_out = "sportapp/templates/sportapp/02-gov_month-out.docx"
        doc1 = Document(file_name)
        for tourney in tourney_list:
            row1 = doc1.tables[2].add_row()
            str_date = unicode(localize(tourney.date_start)).split(" ")
            run11 = row1.cells[0].paragraphs[0].add_run(str_date[0] + " " + str_date[1])
            run11.bold = True
            run11.italic = True
            if tourney.date_end and tourney.date_end != tourney.date_start:
                end_date = unicode(localize(tourney.date_end)).split(" ")
                p11b = row1.cells[0].add_paragraph()
                p11b.alignment = align.CENTER
                run11b = p11b.add_run(" - " + end_date[0] + " " + end_date[1])
                run11b.bold = True
                run11b.italic = True
            row1.cells[0].paragraphs[0].alignment = align.CENTER
            row1.cells[1].paragraphs[0].text = tourney.title
            run21 = row1.cells[2].paragraphs[0].add_run(tourney.time_text)
            run21.bold = True
            row1.cells[2].paragraphs[0].alignment = align.CENTER
            p22 = row1.cells[2].add_paragraph(unicode(tourney.location))
            p22.alignment = align.CENTER
            if tourney.resp_gov != None:
                run31 = row1.cells[3].paragraphs[0].add_run(unicode(tourney.resp_gov))
                run31.bold = True
                row1.cells[3].paragraphs[0].alignment = align.CENTER
                pp32 = row1.cells[3].add_paragraph(unicode(tourney.resp_gov.position))
                pp32.alignment = align.CENTER
        for row in doc1.tables[2].rows:
            for cell in row.cells:
                paragraphs = cell.paragraphs
                for paragraph in paragraphs:
                    for run in paragraph.runs:
                        font = run.font
                        font.size= Pt(12)
        #doc1.save(file_out)
        f = StringIO()
        docx_title = "gov_week_" + str(select_week) + ".docx"
        doc1.save(f)
        length = f.tell()
        f.seek(0)
        response = HttpResponse(
            f.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename=' + docx_title
        response['Content-Length'] = length
        return response
    # /end export block
    context = {'tourney_list': tourney_list,
               'year': year, 'month': month, 'week': week,
               'weeks': weeks,
               'current_week': current_week,
               'next_week': next_week,
               'prev_week': prev_week,
               } 
    return render(request, 'sportapp/list.html', context)
    
@permission_required('sportapp.change_tourney')
def list_edit(request, year=None, month=None, week=None):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    sports = Sport.objects.all()
    sports_list = []
    
    if year:
        tourney_list = Tourney.objects.filter(date_start__year=year)
    if month:
        tourney_list = tourney_list.filter(date_start__month=month)
    if week:
        tourney_list = tourney_list.filter(date_start__week=week)
    tourney_list = tourney_list.order_by("date_start")

    for sp in sports:
          value = '%s' % (sp.title)
          sp_dict = {'id': sp.id, 'label': value, 'value': value}
          sports_list.append(sp_dict)
    sports_js = json.dumps(sports_list)

    formset = TourneyFormSet(request.POST, queryset=tourney_list)
    if request.method == 'POST':
        formset = TourneyFormSet(request.POST, request.FILES, queryset=tourney_list)
        if formset.is_valid():
            formset.save()
            return redirect('list_week', year=year, week=week)
    else:
        formset = TourneyFormSet(queryset=tourney_list)
    context = {'formset': formset, 'sports_js': sports_js,
          'year': year, 'month': month, 'week': week}
    return render(request, 'sportapp/list_edit.html', context)
    
@permission_required('sportapp.change_tourney')
def edit(request,  tourney_id):
    tourney = Tourney.objects.get(id=tourney_id)
    form = TourneyForm(request.POST, instance=tourney)
    if request.method == 'POST':
        formset = TourneyForm(request.POST, instance=tourney)
        if form.is_valid():
            form.save()
            return redirect('detail', tourney_id=tourney_id)
    else:
        form = TourneyForm(instance=tourney)
    return render(request, 'sportapp/edit.html', {'form': form})
    
def detail(request, tourney_id):
    tourney = Tourney.objects.get(id=tourney_id)
    context = {'tourney': tourney}
    return render(request, 'sportapp/detail.html', context)
	
def month_gov(request):
    tourney_list = Tourney.objects.order_by("date_start")
    context = {'tourney_list': tourney_list}
    return render(request, 'sportapp/month_gov.html', context)
    
@permission_required('sportapp.change_tourney')
def upload(request):
   # if this is a POST request we need to process the form data
    file_name = None
    document = None
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            file_name = request.FILES['file_name']
            document = Document(file_name)
            dt = datetime.now()
            for row in document.tables[2].rows:
                tnew = Tourney()
                tnew.location_id = 1
                tnew.sport_id = 1
                tnew.date_start = dt
                tnew.title = row.cells[1].text
                tnew.time_text = row.cells[2].text
                tnew.save()
            # redirect to a new URL:
            #return HttpResponseRedirect('/sportpro')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UploadForm()

    context = {'form': form, 'file': file_name, 'doc': document}
    return render(request, 'sportapp/form_upload.html', context)