from django.shortcuts import render
from .models import Product
from .models import People

# Create your views here.

def home(request):
    context = {}
    return render(request, 'spl/home.html', context)

def products(request):
    context = {}
    context["products"]= Product.objects.all()
    return render(request, 'spl/products.html', context )

def people(request):
    context = {}
    context["people"]= People.objects.all()
    return render(request, 'spl/people.html', context )

def contactus(request):
    context = {}
    return render(request, 'spl/contactus.html', context)
