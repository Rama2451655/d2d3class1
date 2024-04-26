from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    return HttpResponse('hi hello world')
def d2d3(request):
    return render(request,'d2d3.html')

# Create your views here.
