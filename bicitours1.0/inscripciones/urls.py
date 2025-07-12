
from django.urls import path
from .views import InscripcionCreateView, GraciasTemplateView

app_name = 'inscripciones'

urlpatterns = [
    path('nuevo/', InscripcionCreateView.as_view(), name='nueva'),
    path('gracias/', GraciasTemplateView.as_view(), name='gracias'),
]
