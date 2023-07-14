from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание', blank=True)
    image = models.ImageField(blank=True)


class Measurement(models.Model):

    sensor_id = models.ForeignKey(Sensor,  on_delete=models.CASCADE, related_name='measurements')
    temp = models.FloatField(verbose_name='Измеренная температура')
    date_and_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время измерения')
