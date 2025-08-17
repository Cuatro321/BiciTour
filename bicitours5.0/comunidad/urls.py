from django.urls import path
from . import views

app_name = 'comunidad'

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_publicaciones'),
    path('nueva/', views.nueva_publicacion, name='nueva_publicacion'),
    path('<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('<int:pk>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('<int:pk>/comentar/', views.agregar_comentario, name='agregar_comentario'),
    path('comentario/<int:pk>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    path('<int:pk>/like/', views.like_publicacion, name='like_publicacion'),
]