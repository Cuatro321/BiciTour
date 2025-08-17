from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import FormularioRegistro, FormularioPerfil
from django.contrib.auth.models import User

class RegistroUsuarioView(CreateView):
    template_name = 'usuarios/registro.html'
    form_class = FormularioRegistro
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Enviar email de bienvenida o notificación aquí si es necesario
        return response

class EditarPerfilView(LoginRequiredMixin, UpdateView):
    form_class = FormularioPerfil
    template_name = 'usuarios/editar_perfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.perfil

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'instance': self.get_object()})
        return kwargs