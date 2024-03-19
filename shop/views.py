from django.shortcuts import render

# Create your views here.

# Ваш файл views.py

import requests
from django.http import HttpResponse


def greetings(request):
    return HttpResponse("Добро пожаловать в наш магазин!")


def cat_fact(request):
    # Получаем данные с API о факте о кошках
    response = requests.get('https://catfact.ninja/fact')
    print(response)
    return HttpResponse(response['fact'])