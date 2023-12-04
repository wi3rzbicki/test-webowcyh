from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from webowe.models import User, Note
import hashlib
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
     password = hashlib.sha256(password.encode("utf-8")).hexdigest()

     user = User(username=username, password = password)
     user.save()

     return JsonResponse({"username": user.username, "password": user.password})

@csrf_exempt
def login(request):
     data = json.loads(request.body)
     username = data["username"]
     password = data["password"]
     password = hashlib.sha256(password.encode("utf-8")).hexdigest()

     try:
          user = User.objects.get(username=username, password=password)
          user.login_count += 1
          return HttpResponse("Logged succesfully", status=200)
     except:
          return HttpResponse("Wrong username or passwor", status=404)
     

@csrf_exempt
def get_notes(request):
          notes = Note.objects.all()

          data =json.loads(request.body)
          username = data["username"]
          password = data["password"]
          min_lenght = data.get["min_lenght", 0]
          password = hashlib.sha256(password.encode("utf-8")).hexdigest()


          try:
               user = User.objects.get(username=username, password=password)
          except:
               return HttpResponse("Wrong username or passwor", status=404)
          
          notes = Note.objects.filter(udrt=user)

          notes_data = []
          for note in notes:
               if note.is_longer_than(min_lenght):
                    notes_data.append((note.content))

          return JsonResponse({"notes": notes_data})