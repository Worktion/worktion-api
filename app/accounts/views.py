""" Imports """
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets, filters
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    PublicProfileSerializer
)
from .permissions import IsOwnerOrReadOnly
User = get_user_model()


class RegisterUser(generics.CreateAPIView):
    """ View to register new Users """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    """ View to list the user register """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserProfile(generics.RetrieveUpdateAPIView):
    """ View of the user Profile """
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class UserProfileSearch(viewsets.ModelViewSet):
    """ View to search users"""
    queryset = User.objects.all()
    serializer_class = PublicProfileSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'username']
