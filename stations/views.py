from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from pagination.settings import BUS_STATION_CSV
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    data = []

    with open(BUS_STATION_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i in reader:
            data.append(i)

    page = int(request.GET.get('page', 1))
    elements_per_page = 10
    paginator = Paginator(data, elements_per_page)
    page_ = paginator.get_page(page)
    content = page_.object_list

    context = {
        'bus_stations': content,
        'page': page_
    }
    return render(request, 'stations/index.html', context)
