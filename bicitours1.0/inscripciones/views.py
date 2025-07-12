from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from .models import Inscripcion
<<<<<<< HEAD

=======
>>>>>>> 0f73c11f9eb71601245e21e94b95bb3e242cd977

class InscripcionCreateView(CreateView):
    model = Inscripcion
    fields = ['recorrido', 'nombre', 'correo', 'telefono', 'ciudad', 'estado']
    template_name = 'inscripciones/inscripcion_form.html'
    success_url = reverse_lazy('inscripciones:gracias')

<<<<<<< HEAD
=======
class InscripcionCreateView(CreateView):
    model = Inscripcion
    fields = ['recorrido', 'nombre', 'correo', 'telefono', 'ciudad', 'estado']
    template_name = 'inscripciones/inscripcion_form.html'
    success_url = reverse_lazy('inscripciones:gracias')

>>>>>>> 0f73c11f9eb71601245e21e94b95bb3e242cd977
    def get_initial(self):
        initial = super().get_initial()
        recorrido_id = self.request.GET.get('recorrido')
        if recorrido_id:
            initial['recorrido'] = recorrido_id
        return initial

class GraciasTemplateView(TemplateView):
    template_name = 'inscripciones/gracias.html'
