from django.forms import ModelForm

from rest_api.models import Url as UrlModel


class Url(ModelForm):
    class Meta:
        model = UrlModel
        fields = ['url']
