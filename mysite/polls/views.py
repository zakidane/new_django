from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, world, at the index")



# Create your views here.
