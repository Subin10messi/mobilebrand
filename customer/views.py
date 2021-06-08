from django.shortcuts import render,redirect
from .forms import UserRegistration,Loginform
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def Registration(request,*args,**kwargs):
    form=UserRegistration()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context["form"]=form
    return render(request, "registration.html", context)


def LoginView(request,*args,**kwargs):
    form=Loginform()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("login success")
                login(request,user)
                return render(request,"indecs.html")
            else:
                print("failed")
                context["form"]=form
    return render(request,"login.html",context)


def Sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

def home(request):
    return render(request,"home.html")



