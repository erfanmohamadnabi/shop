# Generated by Django 5.0 on 2023-12-25 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_shop', '0006_rename_is_pade_order_is_pay_alter_order_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='addres',
            field=models.TextField(blank=True, null=True, verbose_name='ادرس منزل کاربر'),
        ),
    ]
