# Generated by Django 3.2.9 on 2021-11-29 10:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_avg_speed_vehicle_avg_speed'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='vehicle'),
        ),
    ]
