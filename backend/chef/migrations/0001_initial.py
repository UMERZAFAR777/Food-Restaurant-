# Generated by Django 5.1.2 on 2024-10-31 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media')),
                ('chef_name', models.CharField(max_length=100)),
                ('chef_title', models.CharField(max_length=100)),
                ('chef_des', models.TextField()),
            ],
        ),
    ]
