# Generated by Django 3.1.7 on 2021-04-26 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RENTaCAR', '0003_auto_20210426_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='duration_type',
            field=models.CharField(choices=[('day/s', 'Day/s'), ('week/s', 'Week/s'), ('month/s', 'Month/s')], default='day/s', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
