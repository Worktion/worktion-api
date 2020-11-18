from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from .serializers import RoutineSerializer
from .models import Routine


class IsOwner(BasePermission):
    """
    Object-level permission to only allow owners
    get and edit his routines
    """
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id


class RoutineViewSet(viewsets.ModelViewSet):
    """ ViewSet of Routines """
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Routine.objects.filter(user=user)
