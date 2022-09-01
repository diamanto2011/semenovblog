from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *

class LoginView(TemplateView):
    """
    Авторизация пользователя.
    """
    template_name = 'login/login.html'

    def get(self, request, *args, **kwargs): 
        # Проверяем, авторизован пользователь или
        # нет. Если нет, выводим форму, если да,
        # редиректим на админпанель
        user = self.request.user  
        if user.is_authenticated:
            return redirect('admin_panel') 
        context = {
            'login_form': LoginForm(),
        }   
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Авторизация пользователя с редиректом на
        # на админ панель. 
        login_form = LoginForm(request.POST)
        user = authenticate(
            username=request.POST.get('username'), 
            password=request.POST.get('password'),
            )
        if user is not None:            
            login(self.request, user) 
            return redirect('admin_panel')
        else:
            messages.error(self.request, 'Пользователь или пароль введены неверно.')
            return redirect('login')          



class LogoutView(TemplateView):
    """
    Логаут
    """
    def get(self, request, *args, **kwargs):
        user = request.user
        logout(request)
        return redirect('login')