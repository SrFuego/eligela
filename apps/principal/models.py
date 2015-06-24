from django.db import models
from stdimage import StdImageField


class Beneficio(models.Model):

    def image_path(self, filename):
        return "beneficios/{0}/{1}".format(self.descripcion[:50], str(filename))

    def beneficio_imagen_administrador(self):
        if not self.enunciado_imagen:
            return None

        imagenHTML = '<img src="/media/{0}" style="width: 150px" />'.format(
            self.enunciado_imagen)

        return imagenHTML

    beneficio_imagen_administrador.allow_tags = True

    descripcion = models.TextField()
    imagen = StdImageField(upload_to=image_path)

    def __str__(self):
        return self.descripcion


class Colaborador(models.Model):

    def image_path(self, filename):
        return "beneficios/{0}/{1}".format(self.nombre, str(filename))

    def colaborador_imagen_administrador(self):
        if not self.enunciado_imagen:
            return None

        imagenHTML = '<img src="/media/{0}" style="width: 150px" />'.format(
            self.enunciado_imagen)

        return imagenHTML

    colaborador_imagen_administrador.allow_tags = True

    imagen = StdImageField(upload_to=image_path)
    link = models.URLField()
    nombre = models.CharField(max_length=50)

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
