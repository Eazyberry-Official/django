from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {})

def base(request):
    #return HttpResponse('<h2>Blog Home</h2>')
    return render(request, 'base.html', {})

def index(request):
    #return HttpResponse('<h2>Blog Home</h2>')
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})


