from django.contrib import admin
from .models import Like_products,Order,OrderDetail
# Register your models here.

admin.site.register(Like_products)
admin.site.register(Order)
admin.site.register(OrderDetail)
