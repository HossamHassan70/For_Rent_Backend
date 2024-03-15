from django.shortcuts import render
from rest_framework import viewsets, status
# from authApi.models import authi
# from authApi.serializers import AuthiSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from users_api.models import User
from users_api.serializers import UserSerializer

# Create your views here.
class authiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if user.password != password:  # Comparing plaintext passwords
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserSerializer(user)  # Assuming you have a serializer defined
        return Response(serializer.data, status=status.HTTP_200_OK)