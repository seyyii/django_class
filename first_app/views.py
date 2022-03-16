import http
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return render(request,'first_app/index.html' )

def about (request):
    return render(request,'first_app/about.html' )

def contact (request):
    return render(request,'first_app/contact.html' )

def services (request):
    return render(request,'first_app/services.html' )


