from django.shortcuts import render
from user.serializers import UserSerializer
from rest_framework import generics


class CreateUserView(generics.CreateAPIView):
    """Create new user in system"""
    serializer_class=UserSerializer
    


