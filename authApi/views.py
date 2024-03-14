from django.shortcuts import render
from rest_framework import viewsets
from authApi.models import authi
from authApi.serializers import AuthiSerializer
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class authiView(viewsets.ModelViewSet):
    queryset = authi.objects.all()
    serializer_class =  AuthiSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'})
        else:
            return Response({'message': 'Wrong'}, status=400)