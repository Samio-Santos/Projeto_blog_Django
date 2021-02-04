from django.shortcuts import render,get_object_or_404, redirect
from post.models import Post
from comentarios.models import Comentarios, Resposta
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Case, Count, When
from django.contrib import messages
from comentarios.forms import FormComentario, FormResposta
from django.contrib.auth.models import User


def index(request):
    data = {}
    post = Post.objects.order_by('-id').annotate(
        numero_comentarios=Count(
            Case(
                When(comentarios__publicado_comentario=True, then=1)
            )
        )
    ).filter(publicado_post=True)

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

    if not post.publicado_post:
        raise Http404()

    if request.method == 'POST':
        if form.is_valid():
            if not request.user.is_authenticated:
                comentario = Comentarios(**form.cleaned_data)
                comentario.post_comentario = post
                comentario.save()
                messages.success(request, 'Comentário enviado com sucesso!')

            else:
                comentario = Comentarios(**form.cleaned_data)
                comentario.post_comentario = post
                comentario.usuario_comentario =  User.objects.get(id=request.POST.get('user_id'))
                comentario.save()
                messages.success(request, 'Comentário enviado com sucesso!')
            
        if formResp.is_valid():
            resposta = Resposta(**formResp.cleaned_data)
            resposta.profile = User.objects.get(id=request.POST.get('user_id'))
            resposta.resposta_comentario = Comentarios.objects.get(id=request.POST.get('comment_id'))
            resposta.save()
            formResp = FormResposta()

    data['post'] = post
    data['form'] = form
    data['comments'] = comments
    
    data['resp'] = resp
    data['formResp'] = formResp
    
    return render(request, 'posts/post.html', data)



def post_categoria(request, categoria):
    data = {}
    post = Post.objects.order_by('-id').filter(categoria_post__nome_cat__iexact=categoria)

    paginator = Paginator(post, 4)
    page = request.GET.get('p')
    post = paginator.get_page(page)

    data['posts'] = post

    return render(request, 'posts/categoria_post.html', data)


def busca_post(request):
    data = {}
    termo = request.GET.get('termo')

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

     )
     
    # cria paginações na minha agenda
    paginator = Paginator(contatos, 4)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    data['posts'] = contatos
    return render(request, 'posts/busca_post.html', data)