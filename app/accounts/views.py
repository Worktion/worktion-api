from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import generics
User = get_user_model()

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
