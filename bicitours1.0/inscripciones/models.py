from django.db import models
from recorridos.models import Recorrido

<<<<<<< HEAD
=======
"""

>>>>>>> 0f73c11f9eb71601245e21e94b95bb3e242cd977
class Inscripcion(models.Model):
    recorrido = models.ForeignKey(
        Recorrido,
        on_delete=models.CASCADE,
        limit_choices_to={'realizado': False}, 
        related_name='inscripciones'
    )
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} → {self.recorrido}"
