from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    biografia = models.TextField(blank=True)
    imagem = models.ImageField(blank=True, upload_to='fotoPerfil')
