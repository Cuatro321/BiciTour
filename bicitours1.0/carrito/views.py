from django.shortcuts import redirect, get_object_or_404
from .models import ItemCarrito
from mercancia.models import Producto
from django.views.generic import ListView
from django.shortcuts import render
#Funcionalidad del carrito es la idea
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.user.is_authenticated:
        item, created = ItemCarrito.objects.get_or_create(producto=producto, usuario=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
        item, created = ItemCarrito.objects.get_or_create(producto=producto, session_key=request.session.session_key)

    if not created:
        item.cantidad += 1
        item.save()

    return redirect('mercancia:lista')


class CarritoListView(ListView):
    model = ItemCarrito
    template_name = 'carrito/carrito_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ItemCarrito.objects.filter(usuario=self.request.user)
        else:
            session_key = self.request.session.session_key
            return ItemCarrito.objects.filter(session_key=session_key)


def carrito_detalle(request):
  
    carrito = request.session.get('carrito', {})
    context = {'carrito': carrito}
    return render(request, 'carrito/carrito_detalle.html', context)
