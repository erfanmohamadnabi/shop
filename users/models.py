from django.db import models

# Create your models here.

class Users(models.Model):
    email_user = models.CharField(max_length=200,verbose_name="شماره تلفن کاربر")

    class Meta:
        verbose_name="کاربر"
        verbose_name_plural="باشگاه مشتریان"

    def __str__(self):
        return (self.email_user)
    