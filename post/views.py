from django.shortcuts import render, get_object_or_404, redirect
from post.models import Post
from comentarios.models import Comentarios, Resposta
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Case, Count, When
from django.contrib import messages
from comentarios.forms import FormComentario, FormResposta
from accounts.models import User
from notificaçoes.models import Notification

from django.http import JsonResponse
from django.core import serializers


def index(request):
    data = {}
    post = Post.objects.order_by('-id').annotate(
        numero_comentarios=Count(
            Case(
                When(comentarios__publicado_comentario=True, then=1)
            )
        )
    ).filter(publicado_post=True)
    
    # Notificações
    # Com o usuario logado irá excultar o mesmo codigo incluido a parte de notificações
    if request.user.is_authenticated:
        user = request.user
        notification = Notification.objects.filter(user_to=user).order_by('-date')
        count = Notification.objects.filter(user_to=user, is_seen=False).update(is_seen=True)

        # Paginação
        paginator = Paginator(post, 4)
        page = request.GET.get('p')
        post = paginator.get_page(page) 

        data['posts'] = post
        data['notifications'] = notification
        data['count_notification'] = count
        return render(request, 'posts/index.html', data)
        
    else:
        # Paginação
        paginator = Paginator(post, 4)
        page = request.GET.get('p')
        post = paginator.get_page(page)

        data['posts'] = post

        return render(request, 'posts/index.html', data)

def post(request, id):
    data = {}

    post = get_object_or_404(Post, id=id)
    form = FormComentario(request.POST or None)
    comments = Comentarios.objects.order_by('-id').filter(
        publicado_comentario=True,
        post_comentario=post
    )

    resp = Resposta.objects.order_by('-id')
    formResp = FormResposta(request.POST or None)

    # Notificações
    # Com o usuario logado irá excultar o mesmo codigo incluido a parte de notificações
    if request.user.is_authenticated:
        user = request.user
        notification = Notification.objects.filter(user_to=user).order_by('-date')
        count = Notification.objects.filter(user_to=user, is_seen=False).update(is_seen=True)
            
        if not post.publicado_post:
            raise Http404()

        if request.method == 'POST':
            if form.is_valid():
                comentario = Comentarios(**form.cleaned_data)
                comentario.post_comentario = post
                comentario.usuario_comentario = User.objects.get(id=request.POST.get('user_id'))
                comentario.save()
                comments_ajax = serializers.serialize("json", [comentario, ])
                return JsonResponse({"new_comment": comments_ajax}, status=200)
                
            if formResp.is_valid():
                resposta = Resposta(**formResp.cleaned_data)
                resposta.profile = User.objects.get(id=request.POST.get('user_id'))
                resposta.resposta_comentario = Comentarios.objects.get(id=request.POST.get('comment_id'))
                resposta.save()
                return redirect('post_detalhe', post.id)


        data['post'] = post
        data['form'] = form
        data['comments'] = comments
        
        data['resp'] = resp
        data['formResp'] = formResp

        data['notifications'] = notification
        data['count_notification'] = count
        return render(request, 'posts/post.html', data)
    
    else:
        if not post.publicado_post:
            raise Http404()

        if request.method == 'POST':
            if form.is_valid():
                comentario = Comentarios(**form.cleaned_data)
                comentario.post_comentario = post
                comentario.save()
                comments_ajax = serializers.serialize("json", [comentario, ])
                return JsonResponse({"new_comment": comments_ajax}, status=200)

        data['post'] = post
        data['form'] = form
        data['comments'] = comments
        data['resp'] = resp

        return render(request, 'posts/post.html', data)



def post_categoria(request, categoria):
    data = {}
    post = Post.objects.order_by('-id').filter(categoria_post__nome_cat__iexact=categoria)

    # Notificações
    # Com o usuario logado irá excultar o mesmo codigo incluido a parte de notificações
    if request.user.is_authenticated:
        user = request.user
        notification = Notification.objects.filter(user_to=user).order_by('-date')
        count = Notification.objects.filter(user_to=user, is_seen=False).update(is_seen=True)


        # Paginação
        paginator = Paginator(post, 4)
        page = request.GET.get('p')
        post = paginator.get_page(page)

        data['notifications'] = notification
        data['count_notification'] = count
        data['posts'] = post
        return render(request, 'posts/categoria_post.html', data)

    else:
        paginator = Paginator(post, 4)
        page = request.GET.get('p')
        post = paginator.get_page(page)

        data['posts'] = post

        return render(request, 'posts/categoria_post.html', data)


def busca_post(request):
    data = {}
    termo = request.GET.get('termo')

    # Notificações
    # Com o usuario logado irá excultar o mesmo codigo incluido a parte de notificações
    if request.user.is_authenticated:
        user = request.user
        notification = Notification.objects.filter(user_to=user).order_by('-date')
        count = Notification.objects.filter(user_to=user, is_seen=False).update(is_seen=True)


        # Verifica se o termo existe ou está vázio, caso esteja vázio, emite uma mensagem de erro
        if termo is None or not termo:
            messages.add_message(
                request, 
                messages.ERROR, 
                'O campo de busca não pode ficar vázio'
            )
            return redirect('index')

        contatos = Post.objects.all().filter(
            # '__icontains' verifica se tem parte do texto que o usuario digitou na busca.

            # 'Q' permite fazer um buscar mais avançada e exata, ou é um ou é outro
            Q(titulo_post__icontains=termo) | Q(autor_post__username__iexact=termo) |
            Q(categoria_post__nome_cat__iexact=termo) | Q(conteudo_post__icontains=termo) |
            Q(resumo_post__icontains=termo), publicado_post=True

        ).order_by('-id')
        
        # cria paginações na minha agenda
        paginator = Paginator(contatos, 4)
        page = request.GET.get('p')
        contatos = paginator.get_page(page)

        data['posts'] = contatos
        data['notifications'] = notification
        data['count_notification'] = count
        return render(request, 'posts/busca_post.html', data)

    else:
        # Verifica se o termo existe ou está vázio, caso esteja vázio, emite uma mensagem de erro
        if termo is None or not termo:
            messages.add_message(
                request, 
                messages.ERROR, 
                'O campo de busca não pode ficar vázio'
            )
            return redirect('index')

        contatos = Post.objects.all().filter(
            # '__icontains' verifica se tem parte do texto que o usuario digitou na busca.

            # 'Q' permite fazer um buscar mais avançada e exata, ou é um ou é outro
            Q(titulo_post__icontains=termo) | Q(autor_post__username__iexact=termo) |
            Q(categoria_post__nome_cat__iexact=termo) | Q(conteudo_post__icontains=termo) |
            Q(resumo_post__icontains=termo), publicado_post=True

        ).order_by('-id')
        
        # cria paginações na minha agenda
        paginator = Paginator(contatos, 4)
        page = request.GET.get('p')
        contatos = paginator.get_page(page)

        data['posts'] = contatos
        return render(request, 'posts/busca_post.html', data)



def delete_notification(request, id):
    url = request.POST.get('urldinamica')
    notification = get_object_or_404(Notification, id=id)
    notification.delete()
    messages.success(request, f'Notificação de "{notification.user_from.first_name} {notification.user_from.last_name}" excluida com sucesso!')
    return redirect(url)
