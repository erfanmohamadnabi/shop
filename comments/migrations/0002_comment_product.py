# Generated by Django 5.0 on 2023-12-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000, verbose_name='نظر برای محصول')),
                ('name', models.CharField(max_length=1000, verbose_name='نام و نام خانوادگی')),
                ('rank', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='امتیاز')),
            ],
            options={
                'verbose_name': 'نظرات',
                'verbose_name_plural': 'نظرات محصولات',
            },
        ),
    ]