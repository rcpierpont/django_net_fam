import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "pierzada/home.html")

def about(request):
    return render(request, "pierzada/about.html")

def contact(request):
    return render(request, "pierzada/contact.html")

#print("http://127.0.0.1:8000/hello/pierzada")
def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'pierzada/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )