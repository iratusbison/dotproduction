from django.shortcuts import render
from .models import Service, Product, About

def home(request):
    services = Service.objects.all()
    return render (request,'dotdeveloper/home.html',{'services': services})

def explore_services(request):
    explores = Service.objects.all()
    return render (request, 'dotdeveloper/explore_service.html', {'explores': explores})

def explore_products(request):
    products = Product.objects.all()
    return render (request, 'dotdeveloper/product_list.html',{'products':products})

def about(request):
    abouts = About.objects.all()

    return render (request, 'dotdeveloper/about_us.html',{'abouts':abouts})