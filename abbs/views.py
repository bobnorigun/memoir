
from django.shortcuts import render
from abbs.models import Genre, Book, PapaAbb
from blog.models import Post
import requests
import pandas as pd

def about(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    # papaabb 내용 추가.
    num_posts = Post.objects.all().count()
    num_abbs = PapaAbb.objects.all().count()
    # book instance와 author 내용은 제외.
    url = 'https://docs.google.com/spreadsheets/d/1xHLMpzWPP_-fIuMMGM7N8XdSrKh04CMuPzbZkkj_sek/export?format=csv'
    readcsv = pd.read_csv(url)

    context = {
        'num_posts' : num_posts,
        'num_abbs' : num_abbs,
        'read' : readcsv,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'about.html', context=context)

def privacypolicy(request):
    return render(request, 'privacypolicy.html')

# Create your views here.
from django.views import generic

# 호출하는 페이지 링크는 model명이 앞에 붙고 _list 즉, papaabb_list.html임.
class AbbListView(generic.ListView):
    model = PapaAbb
    ordering = ['-last_modified']

# 레코드가 없으면 자동으로 404페이지 호출.
class AbbDetailView(generic.DetailView):
    model = PapaAbb

# Releasenote 편집화면
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class AbbUpdate(UpdateView):
    model = PapaAbb
    fields = ['releasenote']

import requests
import pandas as pd

def read(request):
    url = 'https://docs.google.com/spreadsheets/d/1xHLMpzWPP_-fIuMMGM7N8XdSrKh04CMuPzbZkkj_sek/export?format=csv'
    readcsv = pd.read_csv(url)
    read = {
        'read' : readcsv
    }

    return render(request, 'read.html', read)

from django.http import HttpResponse, HttpResponseNotFound
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)
