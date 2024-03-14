from rest_framework import serializers
from authApi.models import authi


class AuthiSerializer(serializers.ModelSerializer):
    class Meta:
        model = authi
        fields = '__all__'
