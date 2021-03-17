from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from django.utils import timezone
from django.conf import settings
from notificaçoes.models import Notification

from django.db.models.signals import post_save

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

    # Envia uma notificação ao usuário do comentario caso ele esteja registrado no sistema.
    # Informando que outro usuario respondeu seu comentario.
    def resp_comment(sender, instance, *args, **kwargs):
        resp = instance
        user_from = resp.profile
        user_to = resp.resposta_comentario
        text = resp.resposta[:10]
        if user_from != user_to.usuario_comentario:
            notificacao = Notification(comentario=user_to, user_from=user_from, user_to=user_to.usuario_comentario, text=text, notification_type=2)
            notificacao.save()
            
post_save.connect(Resposta.resp_comment, sender=Resposta)
