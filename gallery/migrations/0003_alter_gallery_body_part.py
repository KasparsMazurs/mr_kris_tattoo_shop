# Generated by Django 3.2.19 on 2023-06-17 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_gallery_body_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='body_part',
            field=models.CharField(choices=[('Leg', 'Leg'), ('Arm', 'Arm'), ('Neck', 'Neck'), ('Torso', 'Torso'), ('Back', 'Back'), ('Palm', 'Palm')], max_length=20),
        ),
    ]
