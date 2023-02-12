from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=1000,choices=(("New",'New'),('Used','Used'),('Refurbished','Refurbished')))
    image_url = models.CharField(max_length=5000,blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    owner=models.ForeignKey(User, on_delete=models.CASCADE,default="")
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    brand=models.ForeignKey('Brand',on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/products/',null=True,blank=True)

    def __str__(self):
        return self.product.name
    class Meta:
        verbose_name_plural='Product Images'


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    logo=models.ImageField(null=True,upload_to='images/categories/')

    def __str__(self):
        return self.category_name        

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.brand_name