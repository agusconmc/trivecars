# Generated by Django 3.1.7 on 2021-04-26 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RENTaCAR', '0004_auto_20210426_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='duration',
            field=models.CharField(max_length=10),
        ),
    ]
