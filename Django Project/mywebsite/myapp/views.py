from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
	return HttpResponse('<h1>Hello World</h1>')

def homepage(request):
	return render(request,'myapp/home.html')


def about(request):
	return render(request,'myapp/about.html')


def contact(request):
	return render(request,'myapp/contact.html')

