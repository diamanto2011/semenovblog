from cProfile import label
from django.forms import fields
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },            
        ),
        label='Имя пользователя',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },            
        ),
        label='Пароль',
    )


