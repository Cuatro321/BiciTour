from django.db import models
from mercancia.models import Producto
from django.contrib.auth.models import User

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        unique_together = ('producto', 'usuario', 'session_key')

    def subtotal(self):
        return self.producto.precio * self.cantidad
