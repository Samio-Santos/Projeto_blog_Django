from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from django.utils import timezone
from django.conf import settings

class Comentarios(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    comentario = models.TextField()
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "comentários"

    def __str__(self):
        return self.nome
    
    def num_resp(self):
        return self.resposta_set.all().count()

class Resposta(models.Model):
    resposta = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    resposta_comentario = models.ForeignKey(Comentarios, on_delete=models.CASCADE)
    data_resposta = models.DateTimeField(default=timezone.now)
    publicado_resposta = models.BooleanField(default=True)
