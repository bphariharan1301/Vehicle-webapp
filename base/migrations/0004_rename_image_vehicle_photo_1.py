# Generated by Django 3.2.9 on 2021-11-29 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_vehicle_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='image',
            new_name='photo_1',
        ),
    ]