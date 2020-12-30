from django.urls import path
from .views import index, post, post_categoria

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:id>', post, name='post_detalhe'),
    path('categoria/<str:categoria>', post_categoria, name='post_categoria'),
]

'''
path('categoria/', post, name='post_categoria'),
path('busca/', post, name='post_busca'),
'''