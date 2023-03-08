import os
from django.http import HttpResponse
from django.shortcuts import render, reverse
from time import gmtime, strftime


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = strftime('%Y-%m-%d %H:%M:%S', gmtime())
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    return HttpResponse(f'Содержимое рабочей директории: {os.listdir(os.getcwd())}')
