# Generated by Django 5.1.2 on 2024-10-31 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_birthday', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_birthday',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
