# Generated by Django 5.0 on 2023-12-23 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_materials_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count_buy',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=20),
            preserve_default=False,
        ),
    ]