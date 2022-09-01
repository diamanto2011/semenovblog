from django.urls import path
from .views import *

urlpatterns = [
    path('', AdminpanelView.as_view(), name='admin_panel'),
]