from django.db import models


class Beneficio(models.Model):
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion


class Colaborador(models.Model):
    nombre = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'colaboradores'


class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    expositor = models.CharField(max_length=50)
    expositorDescripcion = models.TextField()
    video = models.URLField()

    def __str__(self):
        return self.nombre
