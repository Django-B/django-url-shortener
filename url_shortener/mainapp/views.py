from django.shortcuts import render, redirect
from django.http import HttpResponse as HR
from django.urls import reverse

from django.core.handlers.wsgi import WSGIRequest

from random import choice

from .models import Link
from .forms import LinkForm 

def gen_key():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    key = ''.join([choice(chars) for x in range(6)])
    return key
    
def short_link(link, index_url):
    links = Link.objects.all()
    key = gen_key()
    key_exist = bool(links.filter(key=key))
    if not key_exist:
        link = Link(link=link, key=key)
        link.save()
        return index_url+key
    else:
        return short_link(link, index_url)


def index(request: WSGIRequest):
    # if 'links' not in request.session:
    #     request.session['links']=[]

    if request.method == 'POST':
        data = request.POST
        form = LinkForm(data)
        if form.is_valid():
            index_url = request.build_absolute_uri()

            link = form.clean_link()
            new_link = short_link(link, index_url)

            # request.session[links].append([link, new_link])

            data = {
                'link': link,
                'short_link': new_link,
                'error': ''
            }
            return render(request, 'index.html', context=data)
        else:
            data = {
                'link': link,
                'short_link': '',
                'error': 'Некорректный ввод ⌨'
            }
            return render(request, 'index.html', context=data)
        
    return render(request, 'index.html')
    
def redirect_link(request, key):
    links = Link.objects.all()
    link = links.filter(key=key)
    if len(link)>0:
        return redirect(link[0].link)
    else: 
        return redirect('index')
