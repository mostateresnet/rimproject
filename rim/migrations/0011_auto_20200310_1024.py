# Generated by Django 3.0.4 on 2020-03-10 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rim', '0010_equipment_host_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='host_name',
            new_name='hostname',
        ),
    ]
