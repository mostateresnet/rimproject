# Generated by Django 3.0.4 on 2020-03-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rim', '0009_auto_20200309_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='host_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
