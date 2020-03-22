from django.db import models

def upload_path_handler(instance, filename):
    path = 'recurso/' + str(instance.subgrupo).lower()
    extension = '.' + filename.split('.')[1]
    filename = str(instance.id).zfill(5) + extension
    return '{dir}/{file}'.format(dir=path, file=filename)


# Create your models here.
class Grupo(models.Model):
    nombre = models.CharField(max_length=50)

    # configuración para admin
    list_display = ['id', 'nombre']
    list_display_links = ['nombre']
    search_fields = ['nombre']

    class Meta:
        verbose_name_plural = "Grupo"
        verbose_name_plural = "Grupos"

    def __str__(self):
        return self.nombre


class Subgrupo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, blank = True, null = True, verbose_name = 'Categoría')
    nombre = models.CharField(max_length=50)

    list_display = ['id', 'nombre']
    list_display_links = ['nombre']
    search_fields = ['nombre']
    list_filter = ['grupo']

    class Meta:
        verbose_name_plural = "Subgrupo"
        verbose_name_plural = "Subgrupos"

    def __str__(self):
        return self.nombre


class Recurso(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    subgrupo = models.ForeignKey(Subgrupo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    foto = models.FileField(upload_to=upload_path_handler, blank=True, null=True)
    telefono = models.CharField(max_length = 20, verbose_name = 'Teléfono', blank=True, null=True)

    # configuración para admin
    list_display = ['id', 'nombre', 'grupo', 'subgrupo']
    list_display_links = ['nombre']
    search_fields = ['nombre']
    list_filter = ['grupo', 'subgrupo']

    class Meta:
        verbose_name_plural = "Recurso"
        verbose_name_plural = "Recursos"

    def __str__(self):
        return self.nombre
