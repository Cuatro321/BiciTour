from django.contrib import admin
from .models import Recorrido

@admin.register(Recorrido)
class RecorridoAdmin(admin.ModelAdmin):
    list_display = ('ciudad', 'fecha', 'realizado', 'costo')
