from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    thumbnail = models.URLField(max_length=250)
    category = models.ForeignKey('store.Category', on_delete=models.PROTECT)
    price = models.IntegerField()


    def __str__(self):
        pass


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        pass


class Users(models.Model):
    login = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=150)
    avatar = models.IntegerField()
    role = models.CharField(max_length=20)

    def __str__(self):
        pass



