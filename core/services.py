

from urllib import request
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
import random

class CheckUser():
    """
    Различные проверки пользователя.
    """
    def is_auth(self, user):
        # Проверка что пользователь авторизован
        # иначе отправляем на страницу с логином        
        if user.is_authenticated == False:
            return False

class Handlers():
    """
    Различные обработчики
    """
    def file_upload(self, upload_to, filename, file, unique_name=False):
        # Загрузка файлов
        if unique_name == True:
            filename = Handlers.set_unique_name(self, filename)
        with open(f'{upload_to}\{filename}', 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return filename

    def set_unique_name(self, name):
        # Генерация имени файла или любого другого
        # элемента с уникальным префиксом их цифр
        prefix = str(random.randrange(100000000, 999999999, 1))
        return f'{prefix}-{name}'
