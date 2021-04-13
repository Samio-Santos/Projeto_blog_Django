from django.forms import ModelForm
from django.contrib.auth.views import PasswordResetForm
from .models import User
from django.contrib.auth import get_user_model

class Userform(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'biografia', 'imagem')


class EmailValidationPassword(PasswordResetForm):
    def clean_email(self):
        modelUser = get_user_model()
        try:
            email = self.cleaned_data['email']
            user = modelUser.objects.get(email=email)

            if user.email != user.username:
                self.add_error(
                    'email',
                    'Usuário cadastrado com uma rede social.'
                )  
            else:
                return email
                
        except modelUser.DoesNotExist:
            self.add_error(
                'email',
                'Não existi usuario com este e-mail cadastrado.'
            )
            return None
        