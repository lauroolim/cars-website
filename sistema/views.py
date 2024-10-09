from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class Login(View):
    
    def get(self, request):
        contexto = {'mensagem': ''}
        return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/veiculos')
            return redirect(request, 'autenticacao.html', {'mensagem': 'Usuário inativo'})
        return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou senha inválidos'})

class Signup(View):
    
    def get(self, request):
        contexto = {'mensagem': ''}
        return render(request, 'registro.html', contexto)

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username and password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/veiculos')
            except Exception as e:
                return render(request, 'registro.html', {'mensagem': 'Erro ao criar usuário: ' + str(e)})
        return render(request, 'registro.html', {'mensagem': 'Preencha todos os campos'})