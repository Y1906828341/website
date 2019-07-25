from django.shortcuts import render_to_response
from .models import news


# Create your views here.
def index(request):
    context = {}
    context['latest_news'] = news.objects.latest('id')
    return render_to_response('index.html', context)
