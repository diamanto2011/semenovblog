from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import *

# Create your views here.
class SettingsView(TemplateView):
    template_name = 'adminpanel/settings/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_settings'] = SettingsForm()
        return context

