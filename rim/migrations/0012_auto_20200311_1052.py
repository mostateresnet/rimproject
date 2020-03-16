# Generated by Django 3.0.4 on 2020-03-11 15:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rim', '0011_auto_20200310_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='count',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='purchase_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='usb_ports',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='USB ports'),
        ),
    ]
