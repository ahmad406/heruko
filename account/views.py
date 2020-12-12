from django.shortcuts import render , redirect ,HttpResponse
from django.contrib.auth.models import User,auth
from .models import extenduser
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout 
from django.contrib.auth import logout as django_logout

# Create your views here.

    
def signup(request):

    if request.method =="POST":
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        phone =request.POST['phone ']
        password =request.POST['password']
        password2 =request.POST['password2']
        address =request.POST['address']
        city =request.POST['city']
        state =request.POST['state']
        pin_code =request.POST['pin_code']
        email =request.POST['email']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken!")
                return redirect("signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"this email already has account!")
                return redirect("signup")
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name =first_name, last_name=last_name )
                newextenderuser = extenduser (user=user ,phone =phone ,address = address ,city = city , pin_code=pin_code ,state = state )
                newextenderuser.save()
                user.save()
        else:
            messages.info(request,"password not matching..!")
            return redirect("signup")
        return redirect('/ecom/product')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method =="POST":
        login =request.POST['login']
        loginpassword =request.POST['loginpassword']

        user = authenticate(username=login,password=loginpassword)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Successfully Logged In')
            return redirect('/account/signup')
        else:
            messages.error(request,'invalid credentials, Please try again')
            return redirect('/account/signup')
    return HttpResponse('404 - Not Found')



def logout(request):
    django_logout(request)
    return redirect('/account/signup')
    return HttpResponse('404 - Not Found')
   