from django.contrib import admin

from webowe.views import hello
from django.urls import path

urlpatterns = [
    path('hello', hello)
]
