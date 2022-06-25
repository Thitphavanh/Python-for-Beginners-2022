from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def hello(request):
	return HttpResponse('<h1>Hello World</h1>')

def homepage(request):
	products = Product.objects.all()
	allproducts = []
	column = []

	for i,p in enumerate(products, start=1):
		if i % 3==0:
			column.append(p)
			allproducts.append(column)
			column = []

		else:
			column.append(p)

	if len(column) != 0:
		allproducts.append(column)

	context = {'products':allproducts}
		

			
	return render(request,'myapp/home.html', context)
	


def about(request):
	return render(request,'myapp/about.html')


def contact(request):
	return render(request,'myapp/contact.html')

