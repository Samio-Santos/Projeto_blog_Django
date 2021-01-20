from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from django.utils import timezone



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

