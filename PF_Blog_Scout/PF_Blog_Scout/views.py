from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('home.html')
    render = template.render()
    return HttpResponse(render)

def about_us(request):
    template = loader.get_template('about.html')
    render = template.render()
    return HttpResponse(render)

