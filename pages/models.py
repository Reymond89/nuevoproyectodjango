
from django.db import models

# Create your models here.

class page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")     
    content = models.TextField(verbose_name="contenido")
    slug = models.CharField(unique=True, max_length=10, verbose_name="URL amigable")
    visible = models.BooleanField(verbose_name="¿visible?") 
    create_at = models.DateTimeField(auto_now_add=True, verbose_name= "Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

class meta:
    verbose_name = "pagina"
    verbose_name_plural = "paginas"

def __str__(self):
    return self.title
