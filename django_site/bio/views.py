from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    context = {
        'education': Education.objects.order_by('-end_date', '-start_date').all(),
        'experience': Experience.objects.order_by('-end_date', '-start_date').all(),
        'projects': Project.objects.order_by('-end_date', '-start_date').all()
    }
    return render(request, 'bio/Index.html', context)

def resume(request):
    return HttpResponse("<h1>Downloading Resume....</h1>") 