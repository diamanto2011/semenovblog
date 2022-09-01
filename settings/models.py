from django.db import models

class SiteSettingsText(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()


class SiteSettingsBool(models.Model):
    name = models.CharField(max_length=255)
    value = models.BooleanField()


class SiteSettingsFile(models.Model):
    name = models.CharField(max_length=255)
    value = models.BooleanField()
