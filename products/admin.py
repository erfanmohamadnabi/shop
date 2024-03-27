from django.contrib import admin
from .models import Products_Category_Mega, Products_Category, product,Images

class productImagesInline(admin.StackedInline):
    model = Images

class productAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','price','count_buy','active']
    inlines = [productImagesInline]

admin.site.register(product, productAdmin)
admin.site.register(Products_Category_Mega)
admin.site.register(Products_Category)