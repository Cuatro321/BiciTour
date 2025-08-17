# recorridos/views.py
import json
from django.views.generic import ListView, DetailView
from inscripciones.models import Inscripcion
from .models import Recorrido

class RecorridoListView(ListView):
    model = Recorrido
    template_name = 'recorridos/recorrido_list.html'
    context_object_name = 'recorridos'

class RecorridoDetailView(DetailView):
    model = Recorrido
    template_name = 'recorridos/recorrido_detail.html'
    context_object_name = 'recorrido'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        # Trae inscripciones relacionadas a este recorrido
        ctx['inscritos'] = Inscripcion.objects.filter(recorrido=self.object)
        
        # Convierte la ruta en JSON para que JS pueda usarla
        ctx['ruta'] = json.dumps(self.object.ruta or [])
        
        return ctx
