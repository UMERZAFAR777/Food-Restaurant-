# Generated by Django 5.1.2 on 2024-10-31 01:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_Menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='new_menu',
            name='section_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='New_Menu.section'),
            preserve_default=False,
        ),
    ]