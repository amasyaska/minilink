from rest_framework import serializers
from .models import URL


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['long_url', 'short_url', 'clicks']