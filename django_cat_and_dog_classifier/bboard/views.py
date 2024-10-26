from django.http import HttpResponse
from .models import Bb
from django.template import loader

def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    s = 'Объявление воыадваолвыа \r'
    return HttpResponse(template.render(context, request))