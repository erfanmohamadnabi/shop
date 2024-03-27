# Generated by Django 5.0 on 2023-12-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products_Category_Mega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام فارسی دسته بندی مادر')),
                ('enname', models.CharField(max_length=200, verbose_name='نام انگلیسی دسته بندی مادر')),
            ],
            options={
                'verbose_name': 'دسته بندی مادر',
                'verbose_name_plural': 'اضافه کردن دسته بندی مادر محصولات',
            },
        ),
    ]
