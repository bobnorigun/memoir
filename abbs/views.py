
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
import datetime

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
    url = 'https://docs.google.com/spreadsheets/d/1p8JeAXTE2MWTmOZfk3WQK06iA9dkexh-KGvjMpWG_98/export?format=csv'
    # readcsv2 = pd.read_csv(url2, skiprows = [0], usecols = [1,2])
    readcsv2 = pd.read_csv(url, usecols = [1,2,3,4,5])
    length = len(readcsv2)
    # bottom = pd.read_csv(url, nrows=1)
    # lastrow = readcsv2.iloc[: , :-1] 이건 1번 칼럼을 가져옴
    context = {
        'length' : length,
        'read2' : readcsv2,
        'bottom' : readcsv2.tail(1),
        'cell1' : readcsv2['Name'][int(length)-1],
        # 'cell2' : readcsv2['Rating'][3], 일반 숫자
        'cell2' : readcsv2['SecondColor'][int(length)-1], # 목록 길이는 0부터 시작이라 len-1
        'cell3' : readcsv2['ThirdColor'][int(length)-1],
        'cell4' : readcsv2['FourthColor'][int(length)-1],
        'cell5' : readcsv2['FifthColor'][int(length)-1],
    }

    return render(request, 'read.html', context=context)

from django.http import HttpResponse, HttpResponseNotFound
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)
