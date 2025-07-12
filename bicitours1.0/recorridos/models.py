from django.db import models

#Abigail Yunuen Zacarías García

#Modelo Recorrido donde se muestra el recorrido que se realizó con los detalles correspondientes
#Tipos de campos utilizados CharField, DateField, TimeField, DecimalField, etc
class Recorrido(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField("Estado", max_length=100)
    ciudad = models.CharField("Ciudad", max_length=100)
    km =models.DecimalField("Distancia (km)", max_digits=5, decimal_places=2)
    tiempo_estimado = models.DurationField("Tiempo estimado")
    punto_inicio = models.CharField("Punto de inicio", max_length=200)
    costo = models.DecimalField("Costo ($)", max_digits=8, decimal_places=2)
    descripcion = models.TextField("Descripción")
    foto = models.ImageField("Imagen del recorrido", upload_to='fotos_recorridos/')
    realizado = models.BooleanField("¿Ya se realizó?", default=False)

def __str__(self):
    return f"{self.ciudad} - {self.fecha.strftime('%d/%m/%Y')}"
