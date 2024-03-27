from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
import json
import time
import requests
from jdatetime import date, datetime as jdatetime


current_date = jdatetime.now().date()
date = str(current_date).replace("-","/")

class Products_Category_Mega(models.Model):
    name = models.CharField(max_length=200,verbose_name="نام فارسی دسته بندی مادر")
    enname = models.CharField(max_length=200,verbose_name="نام انگلیسی دسته بندی مادر")

    class Meta:
        verbose_name="دسته بندی مادر"
        verbose_name_plural="اضافه کردن دسته بندی مادر محصولات"

    def __str__(self):
        return (self.name)
    


class Products_Category(models.Model):
    name = models.CharField(max_length=200,verbose_name="نام فارسی دسته بندی")
    mega_category = models.ForeignKey(Products_Category_Mega,verbose_name="دسته بندی مادر",on_delete=models.CASCADE)
    enname = models.CharField(max_length=200,verbose_name="نام انگلیسی دسته بندی")

    class Meta:
        verbose_name="دسته بندی محصولات"
        verbose_name_plural="اضافه کردن دسته بندی محصولات"

    def __str__(self):
        return (self.name)
    
    def get_absolute_url(self):
        return reverse("category_product_page",args=[self.enname])
    
class product(models.Model):
    name = models.CharField(max_length=400,verbose_name="نام محصول")
    title = models.CharField(max_length=400,verbose_name="عنوان محصول")
    text = RichTextField(verbose_name="توضیحات محصول")
    price = models.DecimalField(max_digits=20,decimal_places=0,verbose_name="قیمت محصول (تومان)")
    price_percent = models.DecimalField(max_digits=20,decimal_places=0,verbose_name="قیمت تخفیف خورده محصول (تومان)",blank=True,null=True)
    image = models.ImageField(verbose_name="عکس محصول")
    buy = models.BooleanField(verbose_name="فروش عمده محصول",default=False)
    category = models.ForeignKey(Products_Category,verbose_name="دسته بندی",on_delete=models.CASCADE)
    Weight = models.CharField(max_length=400,verbose_name="وزن محصول ( اختیاری)",blank = True,null = True)
    Materials = models.CharField(max_length=400,verbose_name="مواد تشکیل دهنده محصول ( اختیاری)",blank = True,null = True)
    date = models.CharField(max_length=100,verbose_name="تاریخ",default=date)
    count_buy = models.DecimalField(max_digits=20,decimal_places=0,verbose_name = "تعداد فروش",default = 0)
    active = models.BooleanField(default=True,verbose_name="موجود")
    ranking = models.DecimalField(max_digits=20,decimal_places=0,verbose_name = "امتیاز های محصول",default = 0, editable=False)
    ranking_AVG = models.DecimalField(max_digits=20,decimal_places=0,verbose_name = "رنکینگ محصول",null = True,blank = True,default = 0, editable=False)

    class Meta:
        verbose_name="محصول"
        verbose_name_plural="اضافه کردن محصولات"

    def __str__(self):
        return (self.name)
    
    def get_absolute_url(self):
        return reverse("detail_product",args=[self.id])
        
        
        
class Images (models.Model):
    product_id = models.ForeignKey(product, default=None, related_name='images',on_delete = models.CASCADE)
    image_id = models.ImageField(blank=True)


    class Meta:
        verbose_name="عکس"
        verbose_name_plural="اضافه کردن عکس"