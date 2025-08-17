from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('recorridos/', include('recorridos.urls')),
    path('inscripciones/', include('inscripciones.urls', namespace='inscripciones')),
    path('mercancia/', include('mercancia.urls', namespace='mercancia')),
    path('carrito/', include('carrito.urls', namespace='carrito')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('comunidad/', include('comunidad.urls')),

    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
