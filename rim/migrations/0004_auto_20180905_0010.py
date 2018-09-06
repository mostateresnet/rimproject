# Generated by Django 2.0.4 on 2018-09-05 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rim', '0003_merge_20180905_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='count',
            field=models.IntegerField(blank=True, help_text='Count', null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='cpu',
            field=models.CharField(blank=True, help_text='CPU', max_length=64),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='hard_drive',
            field=models.CharField(blank=True, help_text='Hard Drive', max_length=30),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='manufacturer',
            field=models.CharField(blank=True, help_text='Manufacturer', max_length=30),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='memory',
            field=models.CharField(blank=True, help_text='Memory', max_length=10),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='optical_drive',
            field=models.CharField(blank=True, help_text='Optical Drive', max_length=30),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='other_connectivity',
            field=models.CharField(blank=True, help_text='Other Connectivity', max_length=30),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='physical_address',
            field=models.CharField(blank=True, help_text='Physical Adress', max_length=30),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='purchase_info',
            field=models.CharField(blank=True, help_text='Purchase Info', max_length=100),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='purchase_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Purchase Price', max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='removable_media',
            field=models.CharField(blank=True, help_text='Removable Media', max_length=30),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='serial_no',
            field=models.CharField(help_text='Serial Number', max_length=100),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='service_tag',
            field=models.CharField(blank=True, help_text='Service Tag', max_length=30),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='size',
            field=models.CharField(blank=True, help_text='Size', max_length=10),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='smsu_tag',
            field=models.CharField(blank=True, help_text='SMSU Tag', max_length=30),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='usb_ports',
            field=models.IntegerField(blank=True, help_text='USB Ports', null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='video_card',
            field=models.CharField(blank=True, help_text='Video Card', max_length=30),
        ),
    ]