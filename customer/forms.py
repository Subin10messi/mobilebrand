from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegistration(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]
        widgets={
          "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"})
        }


class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

