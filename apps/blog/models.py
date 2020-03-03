from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Categoría"
        verbose_name_plural = "Categorías"

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "Etiqueta"
        verbose_name_plural = "Etiquetas"

    def __unicode__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Autor ")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=128)
    title = models.CharField(max_length = 50,verbose_name = "Título ")
    tags = models.ManyToManyField(Tag)
    content = RichTextField()
    background_image = models.FileField(blank = True, null = True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    publish_on = models.DateField()
    
    # configuración para admin
    list_display = ('title', 'category', 'tags', 'author', 'publish_on', 'created_on', 'updated_on')
    search_fields = ['title']
    list_filter = ['publish_on', 'created_on']
    date_hierarchy = 'pub_date'

    class Meta:
        verbose_name_plural = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-created_on']

    def __str__(self):
        return self.title

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
