from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    print(request)
    return HttpResponse(f"Hello World!  {request.GET['x']}")