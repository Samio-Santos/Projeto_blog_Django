from django.contrib import admin
from .models import Comentarios

# Register your models here.

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 
    'post_comentario', 'data_comentario', 'publicado_comentario')
    list_editable = ('publicado_comentario',)
    list_display_links = ('id', 'nome', 'email')

admin.site.register(Comentarios, ComentarioAdmin)
