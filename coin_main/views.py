from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request) :
    template_name = 'coin_main/index.html'
    return render(request, template_name)
