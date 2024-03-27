from django.db import models
from django.urls import reverse
# Create your models here.
from ckeditor.fields import RichTextField
import json
import time
import requests
from jdatetime import date, datetime as jdatetime

current_date = jdatetime.now().date()
date = str(current_date).replace("-","/")


# data = requests.get("https://api.keybit.ir/time/")
# info = json.loads(data.text)
# date = info['date']['full']['official']['iso']['fa']
# number = date.replace("-","")




class Blog_Category(models.Model):
    name = models.CharField(max_length=200,verbose_name="نام فارسی دسته بندی")
    en_name = models.CharField(max_length=200,verbose_name="نام انگلیسی دسته بندی")

    class Meta:
        verbose_name="دسته بندی جدید"
        verbose_name_plural="اضافه کردن دسته بندی مقالات"

    def __str__(self):
        return (self.name)
    
    def get_absolute_url(self):
        return reverse("Category_blog_page",args=[self.en_name])



class Blog(models.Model):
    name = models.CharField(max_length=300,verbose_name="نام مقاله")
    title = models.CharField(max_length=300,verbose_name="عنوان مقاله")
    date = models.CharField(max_length=100,verbose_name="تاریخ",default=date)
    image = models.ImageField(verbose_name="تصویر مقاله")
    text = RichTextField(verbose_name="متن مقاله")
    category = models.ForeignKey(Blog_Category,verbose_name="دسته بندی",blank=True,null=True,on_delete=models.CASCADE)
    writer = models.CharField(max_length=100,verbose_name="نام نویسنده")
    wr_image = models.ImageField(verbose_name="تصویر نویسنده")
    about = models.TextField(max_length=300,verbose_name="درباره نویسنده",null=True,blank=True)
    date_number = models.DecimalField(max_digits=20, editable=False,decimal_places=0,default=1,verbose_name="این فیلد  تنظیم شده لطفا تغییر ندهید")
    title_seo = models.CharField(verbose_name = "عنوان برای سئو",max_length = 500)
    meta_seo = models.TextField(verbose_name = "توضیحات متا برای سئو")
    keywords = models.CharField(max_length=500,verbose_name = "کلیدواژه ها را برای سئو وارد کنید (  با علامت , جدا کنید  )")

    
    

    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقالات"

    def __str__(self):
        return (self.name)
    
    def get_absolute_url(self):
        return reverse("blog-details",args=[self.id])
        
        