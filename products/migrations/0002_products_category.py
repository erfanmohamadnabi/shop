# Generated by Django 5.0 on 2023-12-19 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام فارسی دسته بندی')),
                ('enname', models.CharField(max_length=200, verbose_name='نام انگلیسی دسته بندی')),
                ('mega_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products_category_mega', verbose_name='دسته بندی مادر')),
            ],
            options={
                'verbose_name': 'دسته بندی محصولات',
                'verbose_name_plural': 'اضافه کردن دسته بندی محصولات',
            },
        ),
    ]