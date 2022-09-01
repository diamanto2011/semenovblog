from django.db import models

class SiteSettings(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()
