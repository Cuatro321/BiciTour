from django.shortcuts import redirect, get_object_or_404, render
from django.http import JsonResponse
from .models import ItemCarrito
from mercancia.models import Producto
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key

    if request.user.is_authenticated:
        migrar_carrito_sesion_a_usuario(request)
        item, created = ItemCarrito.objects.get_or_create(
            producto=producto,
            usuario=request.user,
            session_key=None
        )
    else:
        item, created = ItemCarrito.objects.get_or_create(
            producto=producto,
            usuario=None,
            session_key=session_key
        )

    if not created:
        item.cantidad += 1
    item.save()

    # Responder JSON si es petición AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'success': True})
    else:
        return redirect('mercancia:lista')


def migrar_carrito_sesion_a_usuario(request):
    if not request.user.is_authenticated:
        return

    session_key = request.session.session_key
    if not session_key:
        return

    items_sesion = ItemCarrito.objects.filter(session_key=session_key, usuario=None)
    for item_sesion in items_sesion:
        item_usuario, created = ItemCarrito.objects.get_or_create(
            producto=item_sesion.producto,
            usuario=request.user,
            session_key=None
        )
        if not created:
            item_usuario.cantidad += item_sesion.cantidad
        else:
            item_usuario.cantidad = item_sesion.cantidad
        item_usuario.save()
        item_sesion.delete()


class CarritoListView(ListView):
    model = ItemCarrito
    template_name = 'carrito/carrito_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ItemCarrito.objects.filter(usuario=self.request.user)
        else:
            session_key = self.request.session.session_key
            if not session_key:
                self.request.session.create()
                session_key = self.request.session.session_key
            return ItemCarrito.objects.filter(session_key=session_key)


@login_required
def carrito_detalle(request):
    if request.user.is_authenticated:
        items = ItemCarrito.objects.filter(usuario=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        items = ItemCarrito.objects.filter(session_key=session_key)

    total = sum(item.subtotal() for item in items)

    return render(request, 'carrito/carrito_detalle.html', {'items': items, 'total': total})


@require_POST
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)

    if item.usuario == request.user or item.session_key == request.session.session_key:
        item.delete()

    return redirect('carrito:detalle')


@require_POST
def vaciar_carrito(request):
    if request.user.is_authenticated:
        ItemCarrito.objects.filter(usuario=request.user).delete()
    else:
        session_key = request.session.session_key
        if session_key:
            ItemCarrito.objects.filter(session_key=session_key).delete()

    return redirect('carrito:detalle')


@require_POST
def actualizar_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if item.usuario == request.user or item.session_key == request.session.session_key:
        try:
            cantidad = int(request.POST.get('cantidad', 1))
            if cantidad > 0:
                item.cantidad = cantidad
                item.save()
        except ValueError:
            pass

    return redirect('carrito:detalle')


@require_POST
@login_required
def procesar_compra(request):
    # Aquí podrías agregar lógica para procesar pago, generar pedido, etc.
    # Por ahora solo borramos el carrito y redirigimos
    ItemCarrito.objects.filter(usuario=request.user).delete()
    return redirect('carrito:gracias')


class GraciasView(TemplateView):
    template_name = 'carrito/gracias.html'
