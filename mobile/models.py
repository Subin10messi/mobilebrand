from django.db import models

# Create your models here.

class Brand(models.Model):
    mobile_brand=models.CharField(max_length=100,unique=True)


    def __str__(self):
        return self.mobile_brand

class Product(models.Model):
    mobile_name=models.CharField(max_length=120,unique=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    price=models.IntegerField()
    specs=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images")

    def __str__(self):
        return self.mobile_name


