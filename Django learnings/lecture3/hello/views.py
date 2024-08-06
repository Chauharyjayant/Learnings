from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "hello1/index.html")

def jayant(request):
    return HttpResponse("Nice to meet you this is the second function in the views.py of the app created with the name hello")

def input(request, name):
    return HttpResponse(f"Your name is {name.capitalize()}")