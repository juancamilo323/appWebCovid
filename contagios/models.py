from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

class Departamento(models.Model):
    nombre_departamento =  models.CharField(primary_key = True,max_length=30, verbose_name = 'Departamento')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nombre_departamento

class Documento(models.Model):
    tipodocumento = models.CharField(primary_key = True,max_length=4, verbose_name = 'Tipo de documento')

    class Meta:
        verbose_name = 'Tipo Documento'
        verbose_name_plural = 'Tipo Documentos'

    def __str__(self):
        return self.tipodocumento

class Colombia(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, blank=False, verbose_name = 'Departamento')
    nombres = models.CharField(max_length=30, blank=False, verbose_name = 'Nombres')
    apellidos = models.CharField(max_length=30, blank=False, verbose_name = 'Apellidos')
    tipodocumento = models.ForeignKey(Documento, on_delete=PROTECT, blank=False, verbose_name = 'Tipo de documento')
    numerodocumento = models.CharField(primary_key = True,max_length=15, blank=False, verbose_name = 'Numero de documento')
    correo = models.CharField(max_length=40, blank=False, verbose_name = 'Direccion de correo electronico')
    telofono = models.CharField(max_length=20, blank=False, verbose_name = 'Numero de telefono')
    fecharegistro = models.DateField(null=False, verbose_name = 'Fecha de inicio de cuarentena')
    fechafin = models.DateField(null=False, verbose_name = 'Fecha de fin de cuarentena')

    class Meta:
        verbose_name = 'Contagio'
        verbose_name_plural = 'Contagios'

    def __str__(self):
        return self.numerodocumento