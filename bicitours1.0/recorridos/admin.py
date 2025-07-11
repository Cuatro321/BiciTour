from django.contrib import admin
from .models import Recorrido

#Abigail Yunuen Zacarías García
#Registro del modelo Recorrido en el panel de administración
#Personalización y visualización en la lista de objetos
@admin.register(Recorrido)
class RecorridoAdmin(admin.ModelAdmin):
    list_display = ('ciudad', 'fecha', 'realizado', 'costo')
