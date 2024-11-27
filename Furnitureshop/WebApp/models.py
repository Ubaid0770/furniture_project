from django.db import models

# Create your models here.

class Contactclass(models.Model):
    firstname=models.CharField(max_length=100,null=True,blank=True)
    lastname=models.CharField(max_length=100,null=True,blank=True)
    contact=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    message=models.TextField(max_length=100,null=True,blank=True)

class Signinclass(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    contact=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    repeat=models.CharField(max_length=100,null=True,blank=True)

class Cartclass(models.Model):
    quantity=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    totalprice=models.IntegerField(null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    productname=models.CharField(max_length=100,null=True,blank=True)


class checkoutclass(models.Model):
    firstname = models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    place=models.CharField(max_length=100,null=True,blank=True)
    address=models.TextField(max_length=200,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    total=models.IntegerField(null=True,blank=True)
    message=models.TextField(max_length=200,null=True,blank=True)
  