# Generated by Django 3.2.16 on 2023-02-03 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auto', '0002_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='carad',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
        migrations.AlterField(
            model_name='carad',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CarAd', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
