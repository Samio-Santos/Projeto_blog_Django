from django.forms import ModelForm
from .models import Comentarios

class FormComentario(ModelForm):
    class Meta:
        model = Comentarios
        fields = ('nome', 'email', 'comentario')