import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

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