# Generated by Django 3.2.19 on 2023-06-17 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_gallery_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]