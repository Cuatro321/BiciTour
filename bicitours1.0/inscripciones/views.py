from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from .models import Inscripcion


class InscripcionCreateView(CreateView):
    model = Inscripcion
    fields = ['recorrido', 'nombre', 'correo', 'telefono', 'ciudad', 'estado']
    template_name = 'inscripciones/inscripcion_form.html'
    success_url = reverse_lazy('inscripciones:gracias')

    def get_initial(self):
        initial = super().get_initial()
        recorrido_id = self.request.GET.get('recorrido')
        if recorrido_id:
            initial['recorrido'] = recorrido_id
        return initial

class GraciasTemplateView(TemplateView):
    template_name = 'inscripciones/gracias.html'
