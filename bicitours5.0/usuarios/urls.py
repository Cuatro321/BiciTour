from django.urls import path
from .views import RegistroUsuarioView, EditarPerfilView
from django.contrib.auth import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('perfil/editar/', EditarPerfilView.as_view(), name='editar_perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]