from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'Posts'), (2, 'Respostas'))

    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, blank=True, null=True, related_name="noti_post")
    comentario = models.ForeignKey('comentarios.Comentarios', on_delete=models.CASCADE, blank=True, null=True, related_name="noti_resp")
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noti_from_user")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noti_to_user")
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    text = models.CharField(max_length=60, blank=True)
    date = models.DateTimeField(default=timezone.now) 
    is_seen = models.BooleanField(default=False)


    
