# Generated by Django 3.2.3 on 2021-05-18 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
