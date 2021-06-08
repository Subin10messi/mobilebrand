"""FebMobile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index,brandcreate,brandlist,brandupdate,brandelete,productcreate,productlist,productdelete,productupdate,productview

urlpatterns = [
    path("home",index,name="home"),
    path("create",brandcreate,name="create"),
    path("list",brandlist,name="list"),
    path("update/<int:id>",brandupdate,name="update"),
    path("delete/<int:id>",brandelete,name="delete"),
    path("products",productcreate,name="products"),
    path("items",productlist,name="listproduct"),
    path("deleteprod/<int:id>",productdelete,name="deleteprod"),
    path("produp/<int:id>",productupdate,name="produp"),
    path("details/<int:id>",productview,name="details")
]
