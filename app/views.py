from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,"home.html")

def register(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password =request.POST.get("password")    
        password1=request.POST.get("password1")
        if password==password1:
            print(password,password1)
            User.objects.create_user(username=username,password=password)
            return redirect("login_view")
        else:
            return render(request,"register.html",{"error":"Password doesnoth match"})

    return render(request,'register.html')

def login_view(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password =request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        
        else:
            return HttpResponse("Invalid username of password ")
        
    return render(request,"login.html")

@login_required
def dashboard(request):
    return HttpResponse("You are in dashboard")