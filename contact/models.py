from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام")
    last_name = models.CharField(max_length=100,verbose_name="نام خانوادگی")
    email = models.CharField(max_length=100,verbose_name="ایمیل")
    message = models.TextField(max_length=300,verbose_name="پیام کاربر")

    class Meta:
        verbose_name="پیام"
        verbose_name_plural="پیام ها"

    def __str__(self):
        return (self.name)
