from django.shortcuts import render,redirect
from mobile.forms import BrandCreate
from mobile.models import Brand

# Create your views here.


def index(request):
    return render(request,"index.html")

def brandcreate(request):
    if request.method=="GET":
        form=BrandCreate()
        context={}
        context["form"]=form
        return render(request,"brandcreate.html",context)
    elif request.method=="POST":
        form=BrandCreate(request.POST)
        if form.is_valid():
            mobile_brand=form.cleaned_data.get("mobile_brand")
            brand = Brand(mobile_brand=mobile_brand)
            brand.save()
        return render(request,"index.html")

def brandlist(request):
    brands=Brand.objects.all()
    context={}
    context["brands"]=brands
    return render(request,"brandlist.html",context)

def brandupdate(request,id):
    brand=Brand.objects.get(id=id)
    dict={
        "mobile_brand":brand.mobile_brand
    }
    form=BrandCreate(initial=dict)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BrandCreate(request.POST)
        if form.is_valid():
            mobile_brand=form.cleaned_data.get("mobile_brand")
            brand.mobile_brand=mobile_brand
            brand.save()
        return redirect("list")
    return render(request,"brandedit.html",context)

def brandelete(request,id):
    brand=Brand.objects.get(id=id)
    brand.delete()
    return redirect("list")



