# Generated by Django 5.0 on 2023-12-19 22:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='نام محصول')),
                ('title', models.CharField(max_length=400, verbose_name='عنوان محصول')),
                ('text', ckeditor.fields.RichTextField(verbose_name='توضیحات محصول')),
                ('price', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='قیمت محصول (تومان)')),
                ('price_percent', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True, verbose_name='قیمت تخفیف خورده محصول (تومان)')),
                ('image', models.ImageField(upload_to='', verbose_name='عکس محصول')),
                ('buy', models.BooleanField(default=False, verbose_name='فروش عمده محصول')),
                ('date', models.CharField(max_length=300, verbose_name='تاریخ')),
                ('date_number', models.DecimalField(decimal_places=0, default=14020929, max_digits=20, verbose_name='این فیلد  تنظیم شده لطفا تغییر ندهید')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'اضافه کردن محصولات',
            },
        ),
    ]