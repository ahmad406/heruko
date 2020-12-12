from django.shortcuts import render, redirect , HttpResponse
from django.contrib import messages
from .models import feedback

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def feedback(request):
    if request.method =="POST":
        #mail =request.POST['mail']
        mess =request.POST['mess']

        feed= feedback( mess=mess)
        feed.save()
    else:
        messages.info(request,'thanks for your feed')
        
    return HttpResponse('404 - Not Found')
