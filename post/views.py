from django.shortcuts import render,get_object_or_404
from post.models import Post
from django.http import Http404
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    data = {}
    post = Post.objects.order_by('-id')

    paginator = Paginator(post, 2)
    page = request.GET.get('p')
    post = paginator.get_page(page)

    data['posts'] = post
    return render(request, 'categorias/index.html', data)

def post(request, id):
    data = {}

    post = get_object_or_404(Post, id=id)

    if not post.publicado_post:
        raise Http404()
    
    data['post'] = post

    return render(request, 'categorias/post.html', data)


def post_categoria(request, categoria):
    data = {}
    post = Post.objects.order_by('-id').filter(categoria_post__nome_cat__iexact=categoria)

    paginator = Paginator(post, 2)
    page = request.GET.get('p')
    post = paginator.get_page(page)

    data['posts'] = post

    return render(request, 'categorias/categoria_post.html', data)