from django.db import models

# Create your models here.
class Masaje(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    duracion = models.IntegerField()

    def __str__(self):
        return self.nombre