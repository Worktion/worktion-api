from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission
from .serializers import RoutineSerializer, OnlyRoutineSerializer
from .models import Routine


class IsOwner(BasePermission):
    """
    Object-level permission to only allow owners
    get and edit his routines
    """
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id


class RoutineList(generics.ListCreateAPIView):
    """ ListView of Routines """
    queryset = Routine.objects.all()
    serializer_class = OnlyRoutineSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Routine.objects.filter(user=user)


class RoutineDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Detail of Routine """
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Routine.objects.filter(user=user)


