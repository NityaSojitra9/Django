from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Django_page(request):
    return render(request,'d.html')

def Python_page(request):
    return render(request,'p.html')