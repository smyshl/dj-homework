# Generated by Django 4.2.3 on 2023-07-14 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_sensor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
    ]
