from django.contrib import admin

from store.models import Product, Category, Subcategory, Profile, Comment, Order, OrderItem


# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(OrderItem)
