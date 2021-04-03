from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .form import Userform

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('user')
    senha = request.POST.get('password')

    user = auth.authenticate(request, username=usuario, password=senha)
    
    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')

    else:
        auth.login(request, user)
        messages.success(request, f'Seja bem-vindo {user.first_name} {user.last_name}!')
        return redirect('dashboard')

def logout(request):
    auth.logout(request)
    return redirect('login')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('Snome')
    email = request.POST.get('email')
    user = request.POST.get('user')
    senha = request.POST.get('password')
    rsenha = request.POST.get('Rsenha')
    
    # Variaveis para vericar se a senha possui pelo menos:
    # uma letra maiuscula 
    # uma letra minuscula 
    # um numero.
    lower = any(chr.islower() for chr in senha)
    capital = any(chr.isupper() for chr in senha)
    numeric = any(chr.isnumeric() for chr in senha)

    if not nome or not sobrenome or not email or not user or not senha or not rsenha:
        messages.error(request, 'Nenhum campo pode ficar vázio')
        return render(request, 'accounts/cadastro.html')
    
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts/cadastro.html')

    if not capital:
        messages.error(request, 'A senha dever conter pelo menos uma letra maiúscula.')
        return render(request, 'accounts/cadastro.html')

    if not lower:
        messages.error(request, 'A senha dever conter pelo menos uma letra minúscula.')
        return render(request, 'accounts/cadastro.html')

    if not numeric:
        messages.error(request, 'A senha dever conter pelo menos um número.')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 8:
        messages.error(request, 'Senha muito curta! Senha precisa ter no minimo 8 caracteres.')
        return render(request, 'accounts/cadastro.html')

    if senha != rsenha:
        messages.error(request, 'Senhas não são iguais. Tente novamente!')
        return render(request, 'accounts/cadastro.html')

    if len(user) < 6:
        messages.error(request, 'Usuário precisa ter no minimo 6 caracteres')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe!')
        return render(request, 'accounts/cadastro.html')

    
    if User.objects.filter(username=user).exists():
        messages.error(request, 'Usuário já existe!')
        return render(request, 'accounts/cadastro.html')
    
    messages.success(request, 'Usuário registrado com sucesso. Agora faça login!')
    user = User.objects.create_user(username=user, email=email, password=senha, first_name=nome, last_name=sobrenome)

    user.save()

    return redirect('login')


def perfil_usuario(request, id):
    data = {}
    user = User.objects.get(id=id)
    form  = Userform(request.POST or None, request.FILES or None, instance=user)

    data['user'] = user
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados atualizados com sucesso')
            return redirect('dashboard')
    
    else:
        return render(request, 'accounts/perfil_user.html', data)


def locked(request):
    return render(request, 'accounts/locked.html')



