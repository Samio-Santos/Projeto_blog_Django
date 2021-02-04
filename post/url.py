from django.urls import path
from .views import index, post, post_categoria, busca_post

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:id>', post, name='post_detalhe'),
    path('categoria/<str:categoria>', post_categoria, name='post_categoria'),
    path('busca/', busca_post, name='busca_post')
]
