from django.db import models

# Create your models here.

class variable(models.Model):
    latitud = models.FloatField('Latitud (dd)')
    longitud = models.FloatField('Longitud (dd)')
    velocidad = models.FloatField('Velocidad (m/s)')
    altitud = models.FloatField('Altitud (m)')
    rest_bateria = models.FloatField('Bateria restante (%)')
    volt_bateria = models.FloatField('Voltaje bateria (V)')
    curr_bateria = models.FloatField('Corriente bateria (A)')
