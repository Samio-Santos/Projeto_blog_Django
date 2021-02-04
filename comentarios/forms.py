from django import forms
from .models import Comentarios, Resposta

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('nome', 'email', 'comentario')


class FormResposta(forms.ModelForm):
    resposta = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Responder:'}))
    class Meta:
        model = Resposta
        fields = ('resposta',)