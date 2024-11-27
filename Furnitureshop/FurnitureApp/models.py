from django.db import models

# Create your models here.

class Categoryclass(models.Model):
    cname=models.CharField(max_length=100,null=True,blank=True)
    cimage=models.ImageField(upload_to="categorypics",null=True,blank=True)
    cdescription=models.TextField(max_length=100,null=True,blank=True)


class Productclass(models.Model):
    productcategory=models.CharField(max_length=100,null=True,blank=True)
    productname=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    description=models.TextField(max_length=100,null=True,blank=True)
    countryoforigin=models.CharField(max_length=100,null=True,blank=True)
    manufacturedby=models.CharField(max_length=100,blank=True,null=True)
    productimage1=models.ImageField(upload_to="productpictures",null=True,blank=True)
    productimage2=models.ImageField(upload_to="productpictures",null=True,blank=True)
    productimage3=models.ImageField(upload_to="productpictures",null=True,blank=True)
  
     