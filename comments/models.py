from django.db import models
from blog.models import Blog
from products.models import product

# Create your models here.
class Comment_blog(models.Model):
    massage = models.TextField(max_length=200,verbose_name="نظر کاربر")
    blog_id=models.ForeignKey(Blog,on_delete=models.CASCADE,verbose_name="نام مقاله")

    def __str__(self):
        return (self.massage)

    class Meta:
        verbose_name="نظرات"
        verbose_name_plural="نظرات مقالات"

class Comment_product(models.Model):
    comment = models.TextField(verbose_name = "نظر برای محصول",max_length=1000)
    name = models.CharField(verbose_name = "نام و نام خانوادگی",max_length=1000)
    rank = models.DecimalField(max_digits=20,decimal_places=0,verbose_name = "امتیاز")
    product_id = models.ForeignKey(product,on_delete=models.CASCADE,verbose_name="نام محصول",related_name = "comments_counts")

    def __str__(self):
        return (self.comment)

    class Meta:
        verbose_name="نظرات"
        verbose_name_plural="نظرات محصولات"

    