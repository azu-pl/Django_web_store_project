from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    info = models.TextField()

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"

    def __str__(self):
        return f"{self.user}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('store.Category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Podkategoria"
        verbose_name_plural = "Podkategorie"

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    thumbnail = models.ImageField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Podukty"


class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=150)
    avatar = models.ImageField()
    role = models.CharField(max_length=20)

    def __str__(self):
        pass

