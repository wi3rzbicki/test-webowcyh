from django.contrib import admin

from .views import hello, calc, get_users, add_user, login
from django.urls import path

urlpatterns = [
    path('hello/<int:number>', hello),
    path('calc', calc),
    path('get_users', get_users),
    path('add_user', add_user),
    path('login', login)
]
