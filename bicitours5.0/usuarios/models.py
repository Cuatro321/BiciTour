from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    foto = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    ubicacion = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"

# Señal para crear perfil automáticamente al crear usuario
@receiver(post_save, sender=User)
def crear_o_actualizar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
    else:
        # Asegurarse de que el perfil exista antes de intentar guardarlo
        if hasattr(instance, 'perfil'):
            instance.perfil.save()