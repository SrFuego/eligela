# Python imports


# Django imports
from django.db import models


# Local imports


class Colegio(models.Model):
    nombre = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100)
    telefono = models.CharField(blank=True, max_length=9)
    direccion = models.CharField(max_length=100)
    asunto = models.TextField()

    def __str__(self):
        return self.nombre
