from django.contrib import admin
from .models import Inscripcion

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'recorrido', 'correo', 'fecha_inscripcion')
    list_filter = ('recorrido', 'fecha_inscripcion')
    search_fields = ('nombre', 'correo', 'ciudad', 'estado')
