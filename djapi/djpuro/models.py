from django.db import models

# Create your models here.
class categoria(models.Model):
    descripcion = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name_plural = "Categorías"
        verbose_name = "Categoría"
