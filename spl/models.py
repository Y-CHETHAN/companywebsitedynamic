from django.db import models
from django.contrib import admin
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','image')

class People(models.Model):
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=30)
    image = models.ImageField(upload_to='photos/')

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name','designation','image')