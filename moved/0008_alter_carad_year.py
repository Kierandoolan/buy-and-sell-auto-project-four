# Generated by Django 3.2.16 on 2023-02-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0007_auto_20230203_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carad',
            name='year',
            field=models.DateField(),
        ),
    ]
