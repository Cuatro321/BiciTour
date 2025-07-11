from .models import Recorrido
from django.views.generic import ListView
from django.views.generic import DetailView
from inscripciones.models import Inscripcion

#Abigail Yunuen Zacarías García

#Lista y views como se quedo cada modelo ListView  y DetailView

#Vista de cómo se muestra la lista de los recorridos

class RecorridoListView(ListView):
    model = Recorrido
    template_name = 'recorridos/recorrido_list.html'
    context_object_name = 'recorridos'

#Vista que muestra el detalle de un recorrido específico 
class RecorridoDetailView(DetailView):
    model = Recorrido
    template_name = 'recorridos/recorrido_detail.html'
    context_object_name = 'recorrido'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data( **kwargs)
        # Trae sólo las inscripciones de este recorrido
        ctx['inscritos'] = Inscripcion.objects.filter(recorrido=self.object)
        return ctx
    