from django.db import models

# Create your models here.

class Brand(models.Model):
    mobile_brand=models.CharField(max_length=100,unique=True)


    def __str__(self):
        return self.mobile_brand
