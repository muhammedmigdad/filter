from django.shortcuts import render,reverse 
from django.http.response import HttpResponseRedirect
from web.models import *


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    sizs = Size.objects.all()
    
    category = request.GET.get('category')
    size = request.GET.get('size')
    price = request.GET.get('price')
    q = request.GET.get('q')
    
    if q:
        products = products.filter(title__icontains=q)
        
    
    if category:
        category = Category.objects.get(name=category)
        products = products.filter(category=category)
        
    
    if size:
        size = Size.objects.get(name=size)
        products = products.filter(sizs=size)
        

    if price:
        if price == '100-500':
            products = products.filter(price__range=(100, 500))
        elif price == '15000-25000':
            products = products.filter(price__range=(15000,25000))
        elif price == '25000-50000':
            products = products.filter(price__range=(25000, 50000))
        elif price == '50000-150000':
            products = products.filter(price__range=(50000, 150000))
    
    
    context = {
        "categories": categories,
        "products": products,
        "sizs": sizs,
    }
    return render(request, 'web/index.html', context=context)

