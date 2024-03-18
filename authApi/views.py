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
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta

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

        if user.password != password: 
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserSerializer(user)  

        #pay load hna
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'firstName':user.first_name,
            'lastName' : user.last_name,
            'phoneNumber': str(user.phone_number),
            'profilePicture' : user.get_profile_picture_url(),
            'DOB': str(user.birthdate),
            'role': user.role,
            'registration_date':str(user.registration_date)
            # infos zyada
        }

        # JWT 
        refresh = RefreshToken.for_user(user)
        # refresh.set_exp(lifetime=timedelta(hours=1))

        # refresh tk
        refresh['user'] = user_data

        return Response({
            # 'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
