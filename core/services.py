

from urllib import request
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

class CheckUser():
    """
    Различные проверки полльзователя.
    """
    def is_auth(self):
        # Проверка что пользователь авторизован
        # иначе отправляем на страницу с логином
        user = request.user
        if user.is_authenticated == False:
            return redirect('login')