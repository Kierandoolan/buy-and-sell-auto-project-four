# Generated by Django 3.2.16 on 2023-02-03 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0005_rename_number_carad_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carad',
            old_name='phonenumber',
            new_name='number',
        ),
    ]
