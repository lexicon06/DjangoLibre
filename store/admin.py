from django.contrib import admin

from .models import Product, Category, SubCategory, Brand, Store

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Store)
