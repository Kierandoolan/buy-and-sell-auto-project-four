# Generated by Django 3.2.16 on 2023-02-03 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_alter_carad_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carad',
            old_name='number',
            new_name='phonenumber',
        ),
    ]
