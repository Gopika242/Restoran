from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.CharField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.TextField(max_length=100,null=True,blank=True)

class SignUpDb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    pass1=models.CharField(max_length=100,null=True,blank=True)
    re_pass=models.CharField(max_length=100, null=True, blank=True)

class CartDb(models.Model):
 name=models.CharField(max_length=100,null=True,blank=True)
 DishName=models.CharField(max_length=100,null=True,blank=True)
 Price=models.IntegerField(null=True,blank=True)
 Quantity=models.IntegerField(null=True,blank=True)
 Total=models.IntegerField(null=True,blank=True)

class OrderDb(models.Model):
 name=models.CharField(max_length=100,null=True,blank=True)
 email=models.CharField(max_length=100, null=True, blank=True)
 Mobile=models.CharField(max_length=100, null=True, blank=True)
 DishName=models.CharField(max_length=100,null=True,blank=True)
 Price=models.IntegerField(null=True, blank=True)
 Quantity=models.IntegerField(null=True, blank=True)
 TotalAmount=models.IntegerField(null=True, blank=True)
 Address=models.TextField(max_length=200,null=True,blank=True)
