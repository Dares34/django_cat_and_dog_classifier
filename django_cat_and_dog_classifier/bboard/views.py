from django.http import HttpResponse
from .models import Bb
from django.template import loader
from django.shortcuts import render

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'index.html', {'bbs': bbs})