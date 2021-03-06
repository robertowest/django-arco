from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


def upload_post_path_handler(instance, filename):
    path = 'post/' + str(instance.category).lower()
    extension = '.' + filename.split('.')[1]
    filename = str(instance.id).zfill(5) + extension
    return '{dir}/{file}'.format(dir=path, file=filename)


class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Etiqueta"
        verbose_name_plural = "Etiquetas"

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Autor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank = True, null = True, verbose_name = 'Categoría')
    slug = models.SlugField(blank = True, null = True)
    title = models.CharField(max_length = 50, verbose_name = 'Título')
    tags = models.ManyToManyField(Tag)
    content = RichTextField(verbose_name = 'Contenido')
    background_image = models.FileField('Imágen', upload_to=upload_post_path_handler, blank=True, null=True)
    created_on = models.DateField(auto_now_add=True, verbose_name = 'Creado')
    updated_on = models.DateField(auto_now=True, verbose_name = 'Modificado')
    publish_on = models.DateField('Publicado ', blank = True, null = True)
    
    # configuración para admin
    list_display = ['title', 'category', 'publish_on', 'author', 'created_on', 'updated_on']
    list_display_links = ['title']
    exclude = ['slug']
    search_fields = ['title']
    list_filter = ['author']
    date_hierarchy = 'publish_on'

    class Meta:
        verbose_name_plural = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            saved_image = self.background_image
            self.background_image = None
            super(Post, self).save(*args, **kwargs)
            self.background_image = saved_image
        super(Post, self).save(*args, **kwargs)


    # def save(self, *args, **kwargs):
    #     webfile = urllib2.urlopen(self.background_image)
    #     extension = mimetypes.guess_type(self.background_image)[0].split("/")[1]
    #     self.background_image = '%s/image/post/%s.%s' % (settings.BASE_URL,self.slug,extension )
    #     output = open('home/periodic/mnt' + self.background_image ,'w')
    #     output.write(webfile.read())
    #     output.close()
    #     webfile.close()
    #     super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = "Artículo", related_name="article_comments")
    comment_author = models.CharField(max_length = 50, verbose_name = "Nombre")
    comment_content = models.CharField(max_length = 200, verbose_name = "Cometario")
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment_content
