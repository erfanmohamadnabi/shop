# Generated by Django 5.0 on 2023-12-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(max_length=300, verbose_name='پیام کاربر'),
        ),
    ]
