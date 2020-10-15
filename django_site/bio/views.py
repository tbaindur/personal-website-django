from django.shortcuts import render, resolve_url
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    context = {
        'intro': Intro.objects.first(),
        'education': Education.objects.order_by('-end_date', '-start_date').all(),
        'experience': Experience.objects.order_by('-end_date', '-start_date').all(),
        'projects': Project.objects.order_by('-end_date', '-start_date').all(),
        'skill_types': Skill_type.objects.all()
    }
    return render(request, 'bio/Index.html', context)

