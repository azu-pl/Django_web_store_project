from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        pass


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    thumbnail = models.ImageField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.DecimalField()


    def __str__(self):
        pass


class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=150)
    avatar = models.ImageField()
    role = models.CharField(max_length=20)

    def __str__(self):
        pass

