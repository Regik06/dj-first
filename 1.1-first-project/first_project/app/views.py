from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time_view'),
        'Показать содержимое рабочей директории': reverse('workdir_view')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    dt = datetime.datetime.now()
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = dt
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    path = '.'

    rez = sorted(os.listdir(path))
    for n, item in enumerate(rez):
        return n + 1, item
