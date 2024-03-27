from django.contrib import admin
from .models import Blog_Category,Blog

# Register your models here.

admin.site.register(Blog_Category)
admin.site.register(Blog)