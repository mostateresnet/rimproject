# Generated by Django 2.0.4 on 2018-12-06 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rim', '0007_auto_20181206_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]