from django.db import models

class SiteTextSettings(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()


class SiteBooleanSettings(models.Model):
    name = models.CharField(max_length=255)
    value = models.BooleanField(default=False)


class SiteFileSettings(models.Model):
    name = models.CharField(max_length=255)
    value = models.FileField(upload_to='media/')