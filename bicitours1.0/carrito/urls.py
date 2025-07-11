from django.urls import path
from .views import agregar_al_carrito
from .views import CarritoListView
from . import views
#Esto es inicio de la siguiente version añadir carrito y login pendiente
app_name = 'carrito'

urlpatterns = [
    path('', views.carrito_detalle, name='detalle'),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar'),
    path('', CarritoListView.as_view(), name='ver'),
]
