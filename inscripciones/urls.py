
from django.urls import path
from .views import InscripcionCreateView, GraciasTemplateView

"""
Aqui iria la creacion el de finalizacion  de la inscripcion como "Gracias"
"""

app_name = 'inscripciones'

urlpatterns = [
    path('nuevo/', InscripcionCreateView.as_view(), name='nueva'),
    path('gracias/', GraciasTemplateView.as_view(), name='gracias'),
]
