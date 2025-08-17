from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.carrito_detalle, name='detalle'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar'),
    path('ver/', views.CarritoListView.as_view(), name='ver'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar'),
    path('vaciar/', views.vaciar_carrito, name='vaciar'),
    path('actualizar/<int:item_id>/', views.actualizar_carrito, name='actualizar'),
     path('procesar/', views.procesar_compra, name='procesar_compra'),
    path('gracias/', views.GraciasView.as_view(), name='gracias'),
]
