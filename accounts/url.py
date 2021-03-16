from django.urls import path
from .views import login, cadastro, logout, perfil_usuario, locked
from post.views import index

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='register'),
    path('dashboard/', index, name='dashboard'),
    path('logout/', logout , name='logout'),
    path('perfil/<int:id>/', perfil_usuario, name='perfil_user'),
    path('locked/', locked , name='locked'),
]
