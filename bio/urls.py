from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="bio-home"),
    #path('resume/', views.resume, name="bio-resume-download")
]