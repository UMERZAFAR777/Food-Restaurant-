# Generated by Django 5.1.2 on 2024-10-31 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('people', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]