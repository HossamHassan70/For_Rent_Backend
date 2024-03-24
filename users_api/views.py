from rest_framework import viewsets, status
from .models import User
from .serializers import UserSerializer
from authApi.models import UserEmailVerification


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.validation_states = False

        new_verification = UserEmailVerification(email=instance.email)
        new_verification.generateCode()
        new_verification.sendCode()
        instance.save()
