# Generated by Django 5.0 on 2024-01-27 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.CharField(default='1402/11/07', max_length=100, verbose_name='تاریخ'),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.ImageField(blank=True, upload_to='')),
                ('product_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
            options={
                'verbose_name': 'عکس',
                'verbose_name_plural': 'اضافه کردن عکس',
            },
        ),
    ]