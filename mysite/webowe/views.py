from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from webowe.models import User
# Create your views here.

def hello(request):
    print(request)
    return HttpResponse(f"Hello World!  {request.GET['x']}")

@csrf_exempt
def calc(request):
    data = json.loads(request.body)
    if data["operation"]=="+":
          result = data["a"] + data["b"]
    return HttpResponse(f"{result}")

def get_users(request):
     users = User.objects.all()
     users_data=[]
     for user in users:
          users_data.append(user.username)
     return JsonResponse({"users": users_data})


@csrf_exempt
def add_user(request):
     data =json.loads(request.body)
     username = data["username"]
     password = data["password"]

     user = User(username=username, password = password)
     user.save()

     return JsonResponse({"username": user.username, "password": user.password})