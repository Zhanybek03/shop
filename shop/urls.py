from django.contrib import admin
from django.urls import path, include
from shop.views import greetings, cat_fact, list_item, detail_item

urlpatterns = [
    path('greeting/', greetings, name='greeting'),
    path('facts/', cat_fact, name='cat_fact'),
    path('', list_item),
    path('<int:pk>/', detail_item),
]