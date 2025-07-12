from django.urls import path
from .views import RecorridoListView, RecorridoDetailView

#Abigail Yunuen Zacarías García
#LA LISTA Y LOS DETALLES
# recorridos
#Aquí definimos las rutas para ver la lista de recorridos y los detalles

app_name = 'recorridos'

urlpatterns = [
    path('', RecorridoListView.as_view(), name='lista'),
    path('<int:pk>/',RecorridoDetailView.as_view(),name='detalle')
]
