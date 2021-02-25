from django.db import models

# Create your models here.

class Email(models.Model):
    email = models.EmailField()
    email_enviados = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Emails cadastrados"

    def __str__(self):
        return self.email
    
