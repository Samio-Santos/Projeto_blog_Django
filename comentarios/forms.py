from django import forms
from .models import Comentarios, Resposta
import requests

class FormComentario(forms.ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6Le_dXgaAAAAANOEpV9dhHJQfrqCDqaBx-cYyNMC',
                'response': recaptcha_response
            }
        )
        recaptcha_result = recaptcha_request.json()

        print(recaptcha_result)

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome')
        email = cleaned_data.get('email')
        comentario = cleaned_data.get('comentario')

    class Meta:
        model = Comentarios
        fields = ('nome', 'email', 'comentario')


class FormResposta(forms.ModelForm):
    resposta = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Responder:'}))
    class Meta:
        model = Resposta
        fields = ('resposta',)