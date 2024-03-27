# Generated by Django 5.0 on 2024-01-27 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_blog_keywords_blog_meta_seo_blog_title_seo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.CharField(default='1402/11/07', max_length=100, verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_number',
            field=models.DecimalField(decimal_places=0, default=1, editable=False, max_digits=20, verbose_name='این فیلد  تنظیم شده لطفا تغییر ندهید'),
        ),
    ]