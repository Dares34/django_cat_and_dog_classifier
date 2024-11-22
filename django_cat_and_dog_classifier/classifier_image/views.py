from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from .models import PetClassifier
from .forms import PetClassifierForm

def upload_image(request):
    if (request.method == 'POST'):
        form = PetClassifierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect
    else:
        form = PetClassifierForm()
    
    return render(request, 'upload_image.html', {'form': form})