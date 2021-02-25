from django.db import models
from django.contrib.auth.models import User
from categorias.models import Categoria
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os
from notificaçoes.models import Notification
from django.db.models.signals import post_save
from django.contrib.admin.models import LogEntry

# Create your models here.

class Post(models.Model):
    titulo_post = models.CharField(max_length=150)
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=User)
    data_post = models.DateTimeField(default=timezone.now)
    conteudo_post = models.TextField()
    resumo_post = models.TextField()
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True)
    imagem_post = models.ImageField(upload_to='post_img', blank=True, null=True)
    publicado_post = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo_post

    # Redimensiona uma imagem para ser carregada mais rapido
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.resize_imagem(self.imagem_post.name, 720)

    @staticmethod
    def resize_imagem(nome_imagem, nova_largura):
        img_path = os.path.join(settings.MEDIA_ROOT, nome_imagem)
        img = Image.open(img_path) 
        largura, altura = img.size
        nova_altura = round((nova_largura * altura) / largura)

        if largura <= nova_largura:
            img.close()
            return

        nova_imagem = img.resize((nova_largura, nova_altura), Image.ANTIALIAS)
        nova_imagem.save(
            img_path,
            optimize=True,
            quality=70
        )
        nova_imagem.close()
    
    def post_notification(sender, instance, created, **kwargs):
        posts = instance
        post_autor = posts.autor_post
        if created:
            if posts.publicado_post == True:
                for users in User.objects.all():
                    notificacao = Notification(post=posts, user_from=post_autor, user_to=users, text=titulo, notification_type=1)
                    notificacao.save()

post_save.connect(Post.post_notification, sender=Post)
