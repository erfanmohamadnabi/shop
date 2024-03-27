from django.db import models
from products.models import product
from django.contrib.auth.models import User
import json
import time
import requests
from jdatetime import date, datetime as jdatetime
# Create your models here.


current_date = jdatetime.now().date()
date = str(current_date).replace("-","/")

class Like_products(models.Model):
    product_like = models.ForeignKey(product,verbose_name = "علاقه مندی ها",on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name = "ایدی کاربر")


    class Meta:
        verbose_name="علاقه مندی"
        verbose_name_plural="علاقه مندی ها"

    def __str__(self):
        return (self.product_like.name)




class Order(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name = "نام کاربری")
    is_pay = models.BooleanField(verbose_name="واریز شده / نشده",default=False)
    is_post = models.BooleanField(verbose_name="پرداخت درب منزل",default=False)
    is_post_send = models.BooleanField(verbose_name="ارسال با پست",default=False)
    fname = models.CharField(max_length=200,verbose_name="نام کاربر",null = True,blank = True)
    lname = models.CharField(max_length=200,verbose_name="نام خانوادگی کاربر",null = True,blank = True)
    addres = models.TextField(verbose_name = "ادرس منزل کاربر",null = True,blank = True)
    phone = models.CharField(max_length=100,verbose_name="شماره تلفن کاربر",null = True,blank = True)
    note = models.TextField(verbose_name="یاداشت سفارش",null = True,blank = True)
    peyment_date = models.CharField(blank=True,null=True,verbose_name="تاریخ ثبت سفارش",default = date,max_length = 200)

    def total(self):
        num = 0
        for detail in self.orderdetail_set.all():
            num += detail.count * detail.price
        return num
    
    def __str__(self) -> str:
        return f"{self.owner}"
    
    class Meta:
        verbose_name="سفارشات"
        verbose_name_plural="سفارشات"






class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name = "نام کاربری")
    product = models.ForeignKey(product,on_delete=models.CASCADE,verbose_name = "نام محصول")
    count = models.IntegerField(verbose_name="تعداد")
    price = models.IntegerField(verbose_name="قیمت")

    def get_sum(self): 
        return self.count * self.price 
    
    def __str__(self) -> str:
        return f"{self.product}"
    
    class Meta:
        verbose_name="جزییات سفارشات"
        verbose_name_plural="جزییات سفارشات"