# Generated by Django 3.0.1 on 2020-01-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0007_home_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='available_from',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='home',
            name='offered_since',
            field=models.DateTimeField(),
        ),
    ]
