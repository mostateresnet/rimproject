# Generated by Django 2.0.6 on 2018-07-25 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='cpu',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='equipment',
            name='hard_drive',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='equipment',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='equipment',
            name='memory',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='equipment',
            name='optical_drive',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='equipment',
            name='other_connectivity',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='equipment',
            name='physical_address',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='equipment',
            name='purchase_info',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='equipment',
            name='purchase_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='removable_media',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='equipment',
            name='service_tag',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='equipment',
            name='size',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='equipment',
            name='smsu_tag',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='equipment',
            name='usb_ports',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='video_card',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]