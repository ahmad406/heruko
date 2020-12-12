from django.shortcuts import render
from .models import Product
# Create your views here.
def product(request):

    pros = Product.objects.all() 

    return render(request,'product.html',{'pros':pros})


