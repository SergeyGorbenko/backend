import threading

from django.contrib.postgres.fields import ArrayField
from django.db import models
from rest_framework import serializers

from rest_api.utils import get_keywords_from_keywords_generation_server


class CommonModel(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UrlQuerySet(models.QuerySet):
    pass


class UrlManager(models.Manager):
    def get_queryset(self):
        return UrlQuerySet(self.model, using=self._db)


class Url(CommonModel):
    url = models.URLField(max_length=255, unique=True)
    keywords = ArrayField(models.CharField(max_length=255), blank=True, null=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        self.keywords = ['In the process...']
        super().save(*args, **kwargs)
        t = threading.Thread(target=set_keywords, args=[self.url])
        t.setDaemon(True)
        t.start()

    class Meta:
        verbose_name = 'url'
        verbose_name_plural = 'urls'


def set_keywords(*args):
    keywords = get_keywords_from_keywords_generation_server(args[0])
    url_obj = Url.objects.filter(url=args[0])
    url_obj.update(keywords=keywords)

