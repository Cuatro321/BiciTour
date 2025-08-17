from django.urls import path
from .views import ProductoListView, ProductoDetailView

app_name = 'mercancia'

urlpatterns = [
    path('', ProductoListView.as_view(), name='lista'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='detalle'),
]
