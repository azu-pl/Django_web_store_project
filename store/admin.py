from django.contrib import admin
from store.models import Product, Category, Subcategory

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Subcategory)
