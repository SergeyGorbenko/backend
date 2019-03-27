import requests
from rest_framework import serializers

from rest_api.models import Url as UrlModel


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlModel
        fields = [
            'id',
            'url',
            'keywords'
        ]

    def validate(self, data):
        url = requests.get(data['url'])
        if url.ok:
            return data
        else:
            raise serializers.ValidationError('URL is not working.')
