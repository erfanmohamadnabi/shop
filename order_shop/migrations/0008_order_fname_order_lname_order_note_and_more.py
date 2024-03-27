# Generated by Django 5.0 on 2023-12-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_shop', '0007_order_addres'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='fname',
            field=models.CharField(default=1, max_length=200, verbose_name='نام کاربر'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='lname',
            field=models.CharField(default=1, max_length=200, verbose_name='نام خانوادگی کاربر'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.TextField(default=1, verbose_name='یاداشت سفارش'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='peyment_date',
            field=models.CharField(blank=True, default='۱۴۰۲/۱۰/۰۹', max_length=200, null=True, verbose_name='تاریخ ثبت سفارش'),
        ),
    ]