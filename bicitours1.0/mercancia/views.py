from django.views.generic import ListView, DetailView
from .models import Producto

<<<<<<< HEAD
class ProductoListView(ListView):
=======
class ProductoLisView(ListView):
>>>>>>> 0f73c11f9eb71601245e21e94b95bb3e242cd977
    model = Producto
    template_name = 'mercancia/producto_list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.request.GET.get('categoria')
        disponible = self.request.GET.get('disponible')
        precio_max = self.request.GET.get('precio_max')
            
        if categoria:
            queryset = queryset.filter(categoria__icontains=categoria)
        if disponible =='1':
            queryset = queryset.filter(disponible=True)
        if precio_max:
            queryset = queryset.filter(precio__lte=precio_max)

        return queryset
    
<<<<<<< HEAD
class ProductoDetailView(DetailView):
=======
    class ProductoDetailView(DetailView):
>>>>>>> 0f73c11f9eb71601245e21e94b95bb3e242cd977
        model = Producto
        template_name = 'mercancia/producto_detail.html'
        

#Lista y views como se quedo cada modelo ListView  y DetailView