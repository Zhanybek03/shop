from django.shortcuts import render

# Create your views here.

# Ваш файл views.py

import requests
from django.http import HttpResponse

from shop.models import Item, Purchase


def greetings(request):
    return HttpResponse("Добро пожаловать в наш магазин!")


def cat_fact(request):
    # Получаем данные с API о факте о кошках
    response = requests.get('https://catfact.ninja/fact')
    print(response)
    return HttpResponse(response['fact'])


def list_item(request):
    query_set = Item.objects.all()
    list_of_items = [x for x in query_set]

    return render(request, 'list_item.html', {'all_items': list_of_items})


def detail_item(request, pk, *args, **kwargs):
    query_set = Item.objects.filter(pk=pk).first()

    return render(request, 'detail_item.html', {'item': query_set})
