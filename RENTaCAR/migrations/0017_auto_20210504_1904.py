# Generated by Django 3.1.7 on 2021-05-05 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RENTaCAR', '0016_remove_car_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_order',
            name='car',
        ),
        migrations.AddField(
            model_name='car_order',
            name='car_model',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
