from django.shortcuts import render
from django.http import HttpResponse as HR
from django.urls import reverse


from .models import Link


def short_link(link, absolute_url):
    # он должен создать уникальный символьный 6-ти значный ключ в базе данных и привязать к нему ссылку
    # вернуть ссылку типа http://localhost:8000/short/<КЛЮЧ>, которая будет делать переадресацию на введеный сайт
    
    link = Link()


def index(request):
    return render(request, 'index.html')

def short(request):
    absolute_url = request.build_absolute_uri()
    print(absolute_url)
    link = request.POST.get('link', None)
    link = short_link(link, absolute_url)
    return render(request, 'index.html', context={'link': link, 'short_link': link})
    
def redirect_link(request, key):
    pass
