from django.shortcuts import render

# Create your views here.
import csv, io
from django.contrib import messages
from .models import Mylocation
import os, re, math
import pandas as pd
import numpy as np



def distsum(request):
	template = "distsum/fileupload.html"
	data = Mylocation.objects.all()
	loca_count = Mylocation.objects.count()
	prompt = {'order': 'lat,lon', 'loca_count': loca_count}

	if request.method == "GET":
		return render(request, template, prompt)

	csv_file = request.FILES['file']

	if not csv_file.name.endswith('.csv'):
		messages.error(request, '잘못된 파일')

	data_set = csv_file.read().decode('UTF-8')

	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=','):
		_, created = Mylocation.objects.update_or_create(
			lat=column[0],
			lon=column[1]
		)
	context = {}

	return render(request, template, context)

def calc_dist(lat1, lon1, lat2, lon2):
	lat1 = math.radians(lat1)
	lon1 = math.radians(lon1)
	lat2 = math.radians(lat2)
	lon2 = math.radians(lon2)

	delta_lat = lat2 - lat1
	delta_lon = lon2 - lon1

	a = ((math.sin(delta_lat/2))**2) + math.cos(lat1)*math.cos(lat2)*((math.sin(delta_lon/2))**2)
	c = 2 * math.atan2(a**0.5, (1-a)**0.5)

	earth_radius = 6371

	return float(earth_radius * c)

"""아래 수작업으로 불러 온 좌표값들을 자동으로 생성하고 결과값을 뽑아내는 공식을 만들고 싶어요!!!"""

"""pd.read_csv("./distsum/태국0323Maps.csv", engine='python') """
import sqlite3

def caldistview(request):
	aa = sqlite3.connect('./db.sqlite3')
	data = pd.read_sql_query("SELECT * FROM distsum_mylocation", aa)
	"""data = pd.read_csv("./distsum/태국0307Maps.csv", engine='python')"""
	places = len(data)
	mydist = []
	for i in range(len(data)-1):
		mydist.append(calc_dist(data.loc[i,["lat"]],data.loc[i,["lon"]],data.loc[i+1,["lat"]],data.loc[i+1,["lon"]]))
	fdist = np.round(np.sum(mydist),2)

	return render(request, 'distsum/out.html', {'distance': fdist, 'places': places})