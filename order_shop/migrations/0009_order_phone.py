# Generated by Django 5.0 on 2023-12-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_shop', '0008_order_fname_order_lname_order_note_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=1, max_length=100, verbose_name='شماره تلفن کاربر'),
            preserve_default=False,
        ),
    ]
