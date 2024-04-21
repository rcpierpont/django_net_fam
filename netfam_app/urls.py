from django.urls import path
from netfam_app import views

urlpatterns = [
    path("", views.home, name="home"),
]