
from django.urls import path
from .views import InscripcionCreateView, GraciasTemplateView
<<<<<<< HEAD

app_name = 'inscripciones'

=======

"""
Aqui iria la creacion el de finalizacion  de la inscripcion como "Gracias"
"""

app_name = 'inscripciones'

>>>>>>> 0f73c11f9eb71601245e21e94b95bb3e242cd977
urlpatterns = [
    path('nuevo/', InscripcionCreateView.as_view(), name='nueva'),
    path('gracias/', GraciasTemplateView.as_view(), name='gracias'),
]
