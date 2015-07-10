from django.db import models
from stdimage import StdImageField
from embed_video.fields import EmbedVideoField


class Beneficio(models.Model):

    def image_path(self, filename):
        return "beneficios/{0}/{1}".format(self.descripcion[:50],
                                           str(filename))

    def beneficio_imagen_administrador(self):
        if not self.imagen:
            return None

        imagenHTML = '<img src="/media/{0}" style="width: 150px" />'.format(
            self.imagen)

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
        if not self.imagen:
            return None

        imagenHTML = '<img src="/media/{0}" style="width: 75px" />'.format(
            self.imagen
        )

        if ('.jpg' in imagenHTML):
            return imagenHTML.replace('.jpg', '.miniatura.jpg')
        elif ('.jpeg' in imagenHTML):
            return imagenHTML.replace('.jpeg', '.miniatura.jpeg')
        elif ('.png' in imagenHTML):
            return imagenHTML.replace('.png', '.miniatura.png')
        elif ('.gif' in imagenHTML):
            return imagenHTML.replace('.gif', '.miniatura.gif')
        else:
            return imagenHTML

    colaborador_imagen_administrador.allow_tags = True

    imagen = StdImageField(upload_to=image_path,
                           variations={
                               'miniatura': (75, 75)
                           }
                           )
    link = models.URLField()
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'colaboradores'


class Carrera(models.Model):
    def image_path(self, filename):
        return "carreras/{0}/{1}".format(self.nombre, str(filename))

    def carrera_imagen_administrador(self):
        if not self.foto:
            return None

        imagenHTML = '<img src="/media/{0}" style="width: 75px" />'.format(
            self.foto
        )

        if ('.jpg' in imagenHTML):
            return imagenHTML.replace('.jpg', '.miniatura.jpg')
        elif ('.jpeg' in imagenHTML):
            return imagenHTML.replace('.jpeg', '.miniatura.jpeg')
        elif ('.png' in imagenHTML):
            return imagenHTML.replace('.png', '.miniatura.png')
        elif ('.gif' in imagenHTML):
            return imagenHTML.replace('.gif', '.miniatura.gif')
        else:
            return imagenHTML

    carrera_imagen_administrador.allow_tags = True

    nombre = models.CharField(max_length=50)
    foto = StdImageField(upload_to=image_path,
                         variations={'miniatura': (75, 75)}
                         )
    expositor = models.CharField(max_length=50)
    expositor_Descripcion = models.TextField()
    video = EmbedVideoField()
    video_en_vivo = EmbedVideoField(blank=True)
    imagen_en_vivo = StdImageField(upload_to=image_path,
                                   variations={'miniatura': (75, 75)}
                                   )

    def __str__(self):
        return self.nombre
