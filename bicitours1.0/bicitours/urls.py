from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views #Funcionalidad pendiente



#Cuando suban sus partes actualizadas con el push al final del dia si hay errores  se comentaran para manejar una unica version FINAL 1.0

#Sugerencia del   manejo de rutas  
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('recorridos/', include('recorridos.urls')),
    path('inscripciones/', include('inscripciones.urls', namespace='inscripciones')),       #Modificaciones de ruta tentativas posibles                                                                                   
    path('mercancia/', include('mercancia.urls',namespace='mercancia')),                      #errores de sintaxis 
    path('carrito/', include('carrito.urls',namespace='carrito')),


    #Posibles rutas manejo de inicio secion
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]

#Recursos media 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
