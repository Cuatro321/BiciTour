from django.db import models

<<<<<<< HEAD
=======
"""Modelo mercancia
    nombre
    descripcion
    precio
    imagen
    disponible
"""
>>>>>>> 0f73c11f9eb71601245e21e94b95bb3e242cd977
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre



