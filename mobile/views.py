from django.shortcuts import render, redirect
from mobile.forms import BrandModelform, ProdectModelForm
from mobile.models import Brand, Product


# Create your views here.


def index(request):
    return render(request, "home.html")


def brandcreate(request):
    if request.method == "GET":
        form = BrandModelform()
        context = {}
        context["form"] = form
        return render(request, "brandcreate.html", context)
    elif request.method == "POST":
        form = BrandModelform(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "home.html")


def brandlist(request):
    brands = Brand.objects.all()
    context = {}
    context["brands"] = brands
    return render(request, "brandlist.html", context)


def brandupdate(request, id):
    brand = Brand.objects.get(id=id)
    form = BrandModelform(instance=brand)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = BrandModelform(instance=brand, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect("list")
    return render(request, "brandedit.html", context)


def brandelete(request, id):
    brand = Brand.objects.get(id=id)
    brand.delete()
    return redirect("list")


def productcreate(request):
    form = ProdectModelForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = ProdectModelForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        else:
            context["form"]=form
        return render(request, "productcreate.html", context)
    return render(request, "productcreate.html", context)


def productlist(request):
    mobiles = Product.objects.all()
    context = {}
    context["mobiles"] = mobiles
    return render(request, "productlist.html", context)


def get_object(id):
    return Product.objects.get(id=id)

def productupdate(request,*args,**kwargs):
    id=kwargs.get("id")
    product=get_object(id)
    form=ProdectModelForm(instance=product)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProdectModelForm(instance=product,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listproduct")
    return render(request,"productedit.html",context)




def productdelete(request, id):
    mobile = Product.objects.get(id=id)
    mobile.delete()
    return redirect("listproduct")


def productview(request,*args,**kwargs):
    id=kwargs.get("id")
    product=get_object(id)
    context={}
    context["product"]=product
    return render(request,"productview.html",context)
