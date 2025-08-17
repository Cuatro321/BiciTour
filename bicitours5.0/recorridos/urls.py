# recorridos/urls.py
from django.urls import path
from .views import RecorridoListView,RecorridoDetailView

app_name = 'recorridos'

urlpatterns = [
    path('', RecorridoListView.as_view(), name='lista'),
    path('<int:pk>/',RecorridoDetailView.as_view(),name='detalle'),
]
