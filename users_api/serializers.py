from rest_framework import serializers
from users_api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # extra_kwargs = {
        #     'profile_picture': {'required': False},  # Allow the field to be optional
        # }