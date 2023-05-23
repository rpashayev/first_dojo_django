from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def root(request):
    return redirect ('/blogs')
    
def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return redirect ('/')

def show(request, num):
    return HttpResponse(f'placeholder to display blog number: {num}')