# Generated by Django 3.2.16 on 2023-02-03 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0008_alter_carad_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carad',
            old_name='phonenumber',
            new_name='number',
        ),
    ]