import re
from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from web_project import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from pierzada_app.forms import LogMessageForm
from pierzada_app.models import LogMessage



def home(request):
    print(request.user.is_authenticated)
    return render(request, "pierzada/home.html")

def about(request):
    print(request.user.is_authenticated)
    return render(request, "pierzada/about.html")

def contact(request):
    return render(request, "pierzada/contact.html")


def image(request):
    # assumes file is uploaded to /pierzada_app/uploads
    # assumes name of file is known

    #test_n = "capture.png"
    #test_f = open(str(settings.BASE_DIR) + '/pierzada_app/uploads/' + test_n, "w")
    #initial_path = test_f.name
    #print('uploaded path: ' + initial_path)

    # calculate uploaded filepath after moved to filesystem
    #new_path = str(settings.BASE_DIR) + '/pierzada_app/static/pierzada/' + test_n
    #print('new path: ' + new_path)

    # move uploaded file to filesystem and return rendered html page
    #os.rename(initial_path, new_path)
    #test_f.close()

    return render(request, "pierzada/image.html")

#print("http://127.0.0.1:8000/hello/pierzada")

def log_message(request):
    print('at start of new message')
    form = LogMessageForm(request.POST or None)
    
    if request.method == "POST":
        print('at submission of new message')
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "pierzada/log_message.html", {"form": form})
    
class HomeListView(LoginRequiredMixin, ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html', {})