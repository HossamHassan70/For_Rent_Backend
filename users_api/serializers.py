from rest_framework import serializers
from users_api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id", "registration_date")
