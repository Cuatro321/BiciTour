from django.db import models
from django.contrib.auth.models import User
from recorridos.models import Recorrido

class Inscripcion(models.Model):
    recorrido = models.ForeignKey(
        Recorrido,
        on_delete=models.CASCADE,
        limit_choices_to={'realizado': False},
        related_name='inscripciones'
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='inscripciones'
    )
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'recorrido'], name='unique_usuario_recorrido')
        ]
        verbose_name = 'Inscripción'
        verbose_name_plural = 'Inscripciones'

    def __str__(self):
        return f"{self.nombre} → {self.recorrido}"
