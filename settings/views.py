from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from .forms import *
from .default import *
from .models import *
from core.services import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core import *
from django.conf.urls.static import static
from django.contrib import messages


class SettingsView(View):
    template_name = 'adminpanel/settings/settings.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        initials = self.get_settings_initials()
        form_settings = SettingsForm(initials['initials'])
        context = {
            'form_settings': form_settings,
            'images': initials['filenames'],
        }
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs): 
        # Текстовые настройки
        self.set_settings(
            'site_name', 
            request.POST.get('site_name'), 
            'text',
            )
        self.set_settings(
            'site_description', 
            request.POST.get('site_description'), 
            'text',
            )
        self.set_settings(
            'head', 
            request.POST.get('head'), 
            'text',
            )
        self.set_settings(
            'footer', 
            request.POST.get('footer'), 
            'text',
            ) 
        # Загружаемые файлы
        if request.FILES.get('logo'):
            if Validate.file_extention(self, request.FILES.get('logo').name, 'logo') == True:
                self.set_settings(
                    'logo', 
                        {
                        'filename': request.FILES.get('logo').name,
                        'file': request.FILES.get('logo'),
                        }, 
                    'file',
                    )
            else:
                messages.error(self.request, 'Доступны только файлы png, jpg, jpeg.')
        if request.FILES.get('favicon'):
            if Validate.file_extention(self, request.FILES.get('favicon').name, 'favicon') == True:
                self.set_settings(
                    'favicon', 
                        {
                        'filename': request.FILES.get('favicon').name,
                        'file': request.FILES.get('favicon'),
                        }, 
                    'file',
                    )
            else:
                messages.error(self.request, 'Доступны только файлы ico')
        # Настройки Boolean      
        self.set_settings(
            'is_show_count_of_post_in_rubrics', 
            self.set_bool_data(request.POST.get('is_show_count_of_post_in_rubrics')), 
            'boolean',
            )
        return redirect('settings')

    def set_settings(self, settings_name, settings_value, settings_type):
        # Проверяем какой тип настроек, добавляем или обновляем
        # запись в соотствующей таблице
        if settings_type == 'text':
            SiteTextSettings.objects.update_or_create(
                name=settings_name,
                defaults={
                    'name': settings_name,
                    'value': settings_value,
                }
            )
        if settings_type == 'file':
            filename = Handlers.file_upload( #Загрузка файла, возвращает его имя
                self,
                settings.MEDIA_ROOT,
                settings_value['filename'].replace(' ', '_'),
                settings_value['file'],
                unique_name=False, # Если True - имя файла будет уникальным
            )
            SiteFileSettings.objects.update_or_create(
                name=settings_name,
                defaults={
                    'name': settings_name,
                    'value': filename,
                }
            )
        if settings_type == 'boolean':
            SiteBooleanSettings.objects.update_or_create(
                name=settings_name,
                defaults={
                    'name': settings_name,
                    'value': settings_value,
                }
            )

    def set_bool_data(self, checkbox_data):
        # Переводим значение, полученное из чекбокса
        # формы в True или False
        if checkbox_data == 'on':
            return True
        else:
            return False

    def get_settings_initials(self):
        # Получение начальных значений для формы 
        # на странице с настройками
        settings = self.get_settings()
        initials = {
            'site_name': self.get_settings_value(settings, 'site_name'),
            'site_description': self.get_settings_value(settings, 'site_description'),
            'head': self.get_settings_value(settings, 'head'),
            'footer': self.get_settings_value(settings, 'footer'),
            'is_show_count_of_post_in_rubrics': self.get_settings_value(settings, 'is_show_count_of_post_in_rubrics'),
        }
        filenames = {
            'logo': self.get_settings_value(settings, 'logo'),
            'favicon': self.get_settings_value(settings, 'favicon'),
        }
        result = {
            'initials': initials,
            'filenames': filenames,
        }
        return result  
   
    def get_settings_dict(self, settings_list: list):
        # Создаем словарь из пар: "настройка-значение" из
        # таблицы с настройками
        settings_dict = {}
        for item in settings_list:
            settings_dict[item.name] = item.value
        return settings_dict

    def get_settings(self):
        # Получаем список словарей с настройками и объединяем
        # их в один общий.
        text_settings_dict = self.get_settings_dict(SiteTextSettings.objects.all())
        file_settings_dict = self.get_settings_dict(SiteFileSettings.objects.all())
        boolean_settings_dict = self.get_settings_dict(SiteBooleanSettings.objects.all())
        settings = text_settings_dict | file_settings_dict | boolean_settings_dict
        return settings

    def get_settings_value(self, settings:dict, settings_name:str):    
        # Проверяет наличие настройки в словаре со списком настроек
        # Если она есть, то отдает ее значение, если нет,
        # то возвращает пустую строку.    
        if settings_name in settings:
            settings_value = settings[settings_name]
        else:
            settings_value = ''
        return settings_value


