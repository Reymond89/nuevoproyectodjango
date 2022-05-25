
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name='descripcion')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='creado el')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='titulo')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='imagen', upload_to="articles")
    public = models.BooleanField(verbose_name='¿publicado?')
    user = models.ForeignKey(User, editable=False, verbose_name='Usuario', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='categorias', blank =True, related_name="articles")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='creado el')
    update_at = models.DateTimeField(auto_now_add=True, verbose_name='edito el')

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-create_at']

    def __str__(self):
        return self.title