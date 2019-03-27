import requests
from django import forms
from django.core.exceptions import ValidationError
from django.forms import Form

from api.utils import check_url


class UrlForm(Form):
    url = forms.URLField()

    def clean_url(self):
        data = self.cleaned_data['url']
        try:
            content = check_url(data)
            if content.ok:
                return data
            raise ValidationError('Invalid path', code='invalid')
        except requests.exceptions.ConnectionError:
            raise ValidationError('Invalid host', code='invalid')
