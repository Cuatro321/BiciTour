from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Publicacion, FotoPublicacion, Comentario
from .forms import PublicacionForm, FotoPublicacionForm, ComentarioForm
from recorridos.models import Recorrido

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    for pub in publicaciones:
        pub._current_user = request.user
    return render(request, 'comunidad/lista_publicaciones.html', {
        'publicaciones': publicaciones
    })

@login_required
def nueva_publicacion(request):
    if request.method == 'POST':
        publicacion_form = PublicacionForm(request.POST)
        foto_form = FotoPublicacionForm(request.POST, request.FILES)
        
        if publicacion_form.is_valid():
            publicacion = publicacion_form.save(commit=False)
            publicacion.usuario = request.user
            publicacion.save()
            
            if foto_form.is_valid() and request.FILES:
                for file in request.FILES.getlist('imagen'):
                    FotoPublicacion.objects.create(
                        publicacion=publicacion,
                        imagen=file,
                        descripcion=foto_form.cleaned_data.get('descripcion', '')
                    )
            
            messages.success(request, '¡Publicación creada con éxito!')
            return redirect('comunidad:detalle_publicacion', pk=publicacion.pk)
    else:
        publicacion_form = PublicacionForm()
        foto_form = FotoPublicacionForm()
    
    return render(request, 'comunidad/nueva_publicacion.html', {
        'publicacion_form': publicacion_form,
        'foto_form': foto_form,
    })

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    publicacion._current_user = request.user
    
    # Configurar usuario actual para todos los comentarios
    comentarios = publicacion.comentarios.all()
    for comentario in comentarios:
        comentario._current_user = request.user
    
    return render(request, 'comunidad/detalle_publicacion.html', {
        'publicacion': publicacion,
        'comentario_form': ComentarioForm()
    })

@login_required
def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    publicacion._current_user = request.user
    
    if publicacion.puede_eliminar:
        publicacion.delete()
        messages.success(request, 'Publicación eliminada correctamente')
        return redirect('comunidad:lista_publicaciones')
    else:
        messages.error(request, 'No tienes permiso para eliminar esta publicación')
        return redirect('comunidad:detalle_publicacion', pk=publicacion.pk)

@login_required
def agregar_comentario(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.usuario = request.user
            comentario.save()
            messages.success(request, 'Comentario agregado')
    
    return redirect('comunidad:detalle_publicacion', pk=publicacion.pk)

@login_required
def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario._current_user = request.user
    
    if comentario.puede_eliminar:
        publicacion_pk = comentario.publicacion.pk
        comentario.delete()
        messages.success(request, 'Comentario eliminado')
    else:
        messages.error(request, 'No tienes permiso para eliminar este comentario')
    
    return redirect('comunidad:detalle_publicacion', pk=comentario.publicacion.pk)

@login_required
def like_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    
    if request.user in publicacion.likes.all():
        publicacion.likes.remove(request.user)
        liked = False
    else:
        publicacion.likes.add(request.user)
        liked = True
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'liked': liked,
            'count': publicacion.likes.count()
        })
    
    return redirect('comunidad:detalle_publicacion', pk=publicacion.pk)