from django.views.generic import ListView, DetailView
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'mercancia/producto_list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = super().get_queryset()
        nombre = self.request.GET.get('nombre') 
        disponible = self.request.GET.get('disponible')
        precio_max = self.request.GET.get('precio_max')

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if disponible == '1':
            queryset = queryset.filter(disponible=True)
        if precio_max:
            queryset = queryset.filter(precio__lte=precio_max)

        return queryset

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'mercancia/producto_detail.html'
