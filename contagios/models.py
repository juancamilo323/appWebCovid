from django.db import models

# Create your models here.

class Cali(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False)
    cedula = models.CharField(max_length=15, blank=False)
    correo = models.CharField(max_length=40, blank=False)
    comuna = models.CharField(max_length=2, blank=False)
    barrio = models.CharField(max_length=20, blank=False)
    telofono = models.CharField(max_length=20, blank=False)
    fecharegistro = models.DateField(null=False)
    fechafin = models.DateField(null=False)

    class Meta:
        verbose_name = 'cali'
        verbose_name_plural = 'cali'