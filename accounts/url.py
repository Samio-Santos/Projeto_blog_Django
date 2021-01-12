from django.urls import path
from .views import login, cadastro, logout
from post.views import index

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='register'),
    path('dashboard/', index, name='dashboard'),
    path('logout/', logout , name='logout'),

]
