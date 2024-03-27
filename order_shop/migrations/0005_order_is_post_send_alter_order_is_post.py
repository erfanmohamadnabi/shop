# Generated by Django 5.0 on 2023-12-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_shop', '0004_alter_order_is_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_post_send',
            field=models.BooleanField(default=False, verbose_name='ارسال با پست'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_post',
            field=models.BooleanField(default=False, verbose_name='پرداخت درب منزل'),
        ),
    ]
