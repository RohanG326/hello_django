from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
import re


# Create your views here.

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )