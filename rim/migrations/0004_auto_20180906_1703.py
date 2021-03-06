# Generated by Django 2.0.4 on 2018-09-06 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rim', '0003_merge_20180905_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='cpu',
            field=models.CharField(blank=True, max_length=64, verbose_name='CPU'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_model',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rim.EquipmentType'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='serial_no',
            field=models.CharField(max_length=100, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='smsu_tag',
            field=models.CharField(blank=True, max_length=30, verbose_name='SMSU Tag'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='usb_ports',
            field=models.IntegerField(blank=True, null=True, verbose_name='USB Ports'),
        ),
    ]
