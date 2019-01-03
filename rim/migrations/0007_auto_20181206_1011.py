# Generated by Django 2.1.3 on 2018-12-06 16:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion

def forwards(apps, schema_editor):
    Checkout = apps.get_model('rim', 'Checkout')
    Client = apps.get_model('rim', 'Client')
    for c in Checkout.objects.all():
        c.new_client = Client.objects.get_or_create(name=c.client)[0]
        c.save()

def backwards(apps, schema_editor):
    Checkout = apps.get_model("rim", "Checkout")
    for c in Checkout.objects.all():
        c.client = c.new_client.name
        c.save()

class Migration(migrations.Migration):

    dependencies = [
        ('rim', '0006_equipment_latest_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bpn', models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator('[mM8]\\d{8}', "Bearpass number must start with an 'M,' 'm,' or '8,' and followed by eight digits.")])),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='equipmenttype',
            name='type_name',
            field=models.CharField(max_length=30, verbose_name='Equipment Type'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='new_client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rim.Client'),
        ),
        migrations.RunPython(forwards, backwards),
        migrations.AlterField(
            model_name='checkout',
            name='client',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='client',
        ),
        migrations.AlterField(
            model_name='checkout',
            name='new_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rim.Client'),
        ),
        migrations.RenameField(
            model_name='checkout',
            old_name='new_client',
            new_name='client',
        ),
    ]