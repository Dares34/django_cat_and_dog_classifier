from django.http import HttpResponse
from .models import Bb, Rubric
from django.template import loader
from django.shortcuts import render

from django.urls import reverse_lazy
from .forms import BbForm
from django.views.generic.edit import CreateView

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics': rubrics}
    return render(request, 'index.html', context)


def rubric_bbs(request, rubric_id):
    bbs = Bb.objects.filter(rubric = rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics':rubrics, 
               'current_rubric':current_rubric}
    return render(request, 'rubric_bbs.html', context)

class BbCreateView(CreateView):
    template_name = 'bb_create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context
