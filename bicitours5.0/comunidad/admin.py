from django.contrib import admin
from .models import Publicacion, FotoPublicacion, Comentario

class FotoPublicacionInline(admin.TabularInline):
    model = FotoPublicacion
    extra = 1
    fields = ('imagen', 'descripcion', 'fecha_subida')
    readonly_fields = ('fecha_subida',)

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 0
    fields = ('usuario', 'contenido', 'fecha_comentario')
    readonly_fields = ('fecha_comentario',)

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'recorrido', 'fecha_publicacion', 'cantidad_comentarios', 'cantidad_likes')
    list_filter = ('fecha_publicacion', 'recorrido')
    search_fields = ('titulo', 'contenido', 'usuario__username')
    inlines = [FotoPublicacionInline, ComentarioInline]
    
    def cantidad_comentarios(self, obj):
        return obj.comentarios.count()
    cantidad_comentarios.short_description = 'Comentarios'
    
    def cantidad_likes(self, obj):
        return obj.likes.count()
    cantidad_likes.short_description = 'Likes'

@admin.register(FotoPublicacion)
class FotoPublicacionAdmin(admin.ModelAdmin):
    list_display = ('publicacion', 'descripcion', 'fecha_subida')
    list_filter = ('fecha_subida',)
    search_fields = ('publicacion__titulo', 'descripcion')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('publicacion', 'usuario', 'fecha_comentario', 'contenido_corto')
    list_filter = ('fecha_comentario', 'usuario')
    search_fields = ('publicacion__titulo', 'usuario__username', 'contenido')
    
    def contenido_corto(self, obj):
        return obj.contenido[:50] + '...' if len(obj.contenido) > 50 else obj.contenido
    contenido_corto.short_description = 'Contenido'