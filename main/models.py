from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Producto(models.Model):
	TIPO = (
		('A', 'Bebida'),
		('B', 'Botana'),
	)
	nombre = models.CharField("Nombre", max_length=25, unique=True)
	precio = models.FloatField("Precio")
	presentacion = models.CharField(max_length=20)
	tipo = models.CharField(choices=TIPO, max_length=1)


class Puesto(models.Model):
	nombre = models.CharField(max_length=20)
	salario = models.FloatField()


class Trabajador(models.Model):
	nombre = models.CharField(max_length=200)
	puesto = models.ForeignKey(Puesto)
