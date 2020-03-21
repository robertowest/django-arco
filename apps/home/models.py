from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
def upload_path_handler(instance, filename):
    return '{dir}/{file}'.format(dir=instance.section.lower(), file=filename)


class Sections(models.Model):
    SECTION = (('home', 'Inicio'),
               ('nav', 'Nav'),
               ('slides', 'Slides'),
               ('welcome', 'Welcome'),
               ('works', 'Works'),
               ('counter', 'Counter'),
               ('services', 'Services'),
               ('blog', 'Blog'),
               ('team', 'Team'),
               ('testimony', 'Testimony'),
               ('subscribe', 'Subscribe'),
               ('footer', 'Footer'))

    section = models.CharField('Sección', max_length=15, choices=SECTION, default='home')
    label = models.CharField('Etiqueta', max_length=50)
    link = models.CharField(max_length=100, blank=True, null=True)
    text_short = models.CharField('Texto breve', max_length=254, blank=True, null=True)
    text_large = RichTextField(verbose_name="Texto largo", blank=True, null=True)
    image = models.FileField(upload_to=upload_path_handler, blank=True, null=True)
    ordered = models.SmallIntegerField(verbose_name='Ordenación', default=1, blank=True, null=True)
    active = models.BooleanField('Activo', default=1, blank=True, null=True)

    class Meta:
        unique_together = ('section', 'label',)    # clave única
        verbose_name = "Section"
        verbose_name_plural = "Sections"

    def __str__(self):
        return self.label.title()
