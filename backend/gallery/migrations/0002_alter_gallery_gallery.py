# Generated by Django 5.1.2 on 2024-10-31 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='gallery',
            field=models.ImageField(upload_to='media'),
        ),
    ]