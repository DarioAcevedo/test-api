from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del Producto',
        unique=True
    )
    fecha_creado = models.DateTimeField()
    vendido = models.BooleanField(default=False)
 
    def __str__(self):
        return '{}'.format(self.descripcion)
 
    class Meta:
        verbose_name_plural = "Productos"
