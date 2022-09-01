from django.shortcuts import render
from django.views.generic.base import TemplateView

class AdminpanelView(TemplateView):
    template_name = 'adminpanel/admin-panel.html'