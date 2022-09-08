from django.urls import path
from .views import *

urlpatterns = [
    path('', SettingsView.as_view(), name='settings')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)