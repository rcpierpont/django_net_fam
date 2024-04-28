import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import ListView
from pierzada_app.forms import LogMessageForm
from pierzada_app.models import LogMessage

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

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "pierzada/log_message.html", {"form": form})
    
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context