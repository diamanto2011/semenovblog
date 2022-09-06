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

# Create your views here.
class SettingsView(View):
    template_name = 'adminpanel/settings/settings.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form_settings = SettingsForm()
        context = {
            'form_settings': form_settings,
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
            self.set_settings(
                'logo', 
                    {
                    'filename': request.FILES.get('logo').name,
                    'file': request.FILES.get('logo'),
                    }, 
                'file',
                )
        if request.FILES.get('favicon'):
            self.set_settings(
                'favicon', 
                    {
                    'filename': request.FILES.get('favicon').name,
                    'file': request.FILES.get('favicon'),
                    }, 
                'file',
                )
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
                settings.MEDIA_ROOT[0],
                settings_value['filename'],
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

    def get_initals(self):
        pass
