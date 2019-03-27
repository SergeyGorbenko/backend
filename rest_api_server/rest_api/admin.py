from django.contrib import admin

from rest_api.forms import Url as UrlForm
from rest_api.models import Url as UrlModel


class UrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'keywords']
    form = UrlForm

    class Meta:
        model = UrlModel


admin.site.register(UrlModel, UrlAdmin)
