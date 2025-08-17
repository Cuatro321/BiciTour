from django import forms
from .models import Publicacion, FotoPublicacion, Comentario

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['recorrido', 'titulo', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4}),
        }

class FotoPublicacionForm(forms.ModelForm):
    class Meta:
        model = FotoPublicacion
        fields = ['imagen', 'descripcion']
        widgets = {
            'descripcion': forms.TextInput(attrs={'placeholder': 'Describe esta foto...'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Escribe tu comentario...'}),
        }