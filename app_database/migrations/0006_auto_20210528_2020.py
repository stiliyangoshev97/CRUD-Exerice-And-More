# Generated by Django 3.1.3 on 2021-05-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_database', '0005_auto_20210528_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
    ]
