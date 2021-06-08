from django import forms
from.models import Brand,Product

class BrandModelform(forms.ModelForm):
    class Meta:
        model=Brand
        fields=["mobile_brand"]

class ProdectModelForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "specs": forms.Textarea(attrs={"class": "form-control"})

        }

    def clean(self):
        cleaned_data = super().clean()
        price = self.cleaned_data.get("price")
        if price < 500:
            msg = "invalid price"
            self.add_error("price", msg)







