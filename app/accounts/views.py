""" Imports """
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets, filters
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    PublicProfileSerializer,
    LoginSerializer,
    ConfirmEmailSerializer,
)
from .permissions import IsOwnerOrReadOnly
User = get_user_model()


class LoginView(generics.CreateAPIView):
    """ View to get access to system """
    queryset = User.objects.all()
    serializer_class = LoginSerializer


class RegisterUser(generics.CreateAPIView):
    """ View to register new Users """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ConfirmEmailView(generics.CreateAPIView):
    """View to confirm email of user """
    queryset = User.objects.all()
    serializer_class = ConfirmEmailSerializer
    permission_classes = [IsAuthenticated]


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
