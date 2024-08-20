from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import register_user
def login(request):
    
    if request.method=="POST":
        # login(request)
        redirect("dashboard")
        
    return render(request,"myapp/login.html")

def register(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        role = request.POST.get("role")
        id=request.POST.get("id")
        password = request.POST.get("password")
        hash_password = make_password(password)
        new_user=register_user(name=name,email=email,role=role,person_id=id,password=hash_password)
        new_user.save()
        return redirect("login")
    
    return render(request,"myapp/register.html")

# @login_required
def dashboard(request):

    if request.method=="POST":
        return HttpResponse("You are in dashboard")
    
def school_login(request):
    return render(request,"myapp/login.html")
