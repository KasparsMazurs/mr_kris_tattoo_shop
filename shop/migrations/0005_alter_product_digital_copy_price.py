# Generated by Django 3.2.19 on 2023-06-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='digital_copy_price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=6),
        ),
    ]
