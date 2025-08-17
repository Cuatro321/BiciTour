from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from .models import Inscripcion

class InscripcionCreateView(LoginRequiredMixin, CreateView):
    model = Inscripcion
    fields = ['recorrido', 'nombre', 'correo', 'telefono', 'ciudad', 'estado']
    template_name = 'inscripciones/inscripcion_form.html'
    success_url = reverse_lazy('inscripciones:gracias')
    login_url = 'login'  # Redirige a login si no está autenticado

    def get_initial(self):
        initial = super().get_initial()
        recorrido_id = self.request.GET.get('recorrido')
        if recorrido_id:
            initial['recorrido'] = recorrido_id
        return initial

    def form_valid(self, form):
        user = self.request.user
        recorrido = form.cleaned_data['recorrido']

        # Verificar inscripción duplicada
        if Inscripcion.objects.filter(usuario=user, recorrido=recorrido).exists():
            messages.error(self.request, "Ya estás inscrito en este recorrido.")
            return redirect('inscripciones:nueva')  # Cambia esta URL si quieres

        # Asignar usuario antes de guardar
        form.instance.usuario = user
        return super().form_valid(form)

class GraciasTemplateView(TemplateView):
    template_name = 'inscripciones/gracias.html'
