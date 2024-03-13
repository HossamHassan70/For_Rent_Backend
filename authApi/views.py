from django.shortcuts import render
from rest_framework import viewsets
from authApi.models import authi
from authApi.serializers import AuthiSerializer

# Create your views here.
class authiView(viewsets.ModelViewSet):
    queryset = authi.objects.all()
    serializer_class =  AuthiSerializer