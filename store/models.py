import os
from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=15)
    post_code = models.CharField(max_length=6)
    city = models.CharField(max_length=25)
    phone_number = models.DecimalField(decimal_places=0, max_digits=9)
    info = models.TextField(blank=True)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"

    def __str__(self):
        return f"{self.user}, {self.info}"


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
        return f"{self.category}/{self.name}"

    class Meta:
        verbose_name = "Podkategoria"
        verbose_name_plural = "Podkategorie"


def tb_media_path(instance, filename):
    file_extension = filename[(filename.rfind(".", -5, -1))::1]
    return os.path.join("tb", "%s%s" % (instance.name, file_extension)).lower()


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    thumbnail = models.ImageField(upload_to=tb_media_path, blank=True)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return f"{self.name}, {self.subcategory}"

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"



