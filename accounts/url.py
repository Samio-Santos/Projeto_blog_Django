from django.urls import path
from .views import login, cadastro, logout, perfil_usuario, locked
from post.views import index
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='register'),
    path('dashboard/', index, name='dashboard'),
    path('logout/', logout , name='logout'),
    path('perfil/<int:id>/', perfil_usuario, name='perfil_user'),
    path('locked/', locked , name='locked'),

    path('reset_password/', 
    auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        email_template_name='accounts/emai_template.html'
        ), 
    name='reset_password'),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_password_sent.html'), 
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), 
     name='password_reset_confirm'),

    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(
        template_name = 'accounts/reset_password_complete.html'
    ), 
    name='password_reset_complete'),
]
