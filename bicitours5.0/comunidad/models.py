from django.db import models
from django.contrib.auth.models import User
from recorridos.models import Recorrido
from django.urls import reverse

class Publicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    recorrido = models.ForeignKey(Recorrido, on_delete=models.CASCADE, related_name='publicaciones')
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes_publicaciones', blank=True)

    class Meta:
        ordering = ['-fecha_publicacion']
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return f"{self.titulo} por {self.usuario.username}"

    def get_absolute_url(self):
        return reverse('comunidad:detalle_publicacion', kwargs={'pk': self.pk})

    @property
    def puede_eliminar(self):
        if not hasattr(self, '_current_user'):
            return False
        return self._current_user == self.usuario or self._current_user.is_staff

class FotoPublicacion(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='comunidad/fotos/')
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Foto de publicación'
        verbose_name_plural = 'Fotos de publicaciones'

    def __str__(self):
        return f"Foto para {self.publicacion.titulo}"

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha_comentario']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.publicacion.titulo}"

    @property
    def puede_eliminar(self):
        if not hasattr(self, '_current_user'):
            return False
        return self._current_user == self.usuario or self._current_user.is_staff