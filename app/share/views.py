from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, BasePermission
from .serializers import (
    ShareRoutineUserSerializer,
    ShareRoutinePublicSerializer,
    ShareRoutineUserDetailSerializer,
)
from .models import ShareRoutineUser, ShareRoutinePublic


class IsOccupant(BasePermission):
    """
    Object-level permission to only allow occupants
    get his routines
    """
    def has_object_permission(self, request, view, obj):
        return obj.occupant.id == request.user.id


class IsOwner(BasePermission):
    """
    Object-level permission to only allow owner
    get or delete his routines
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner.id == request.user.id


class ReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class ShareRoutineUserList(generics.ListCreateAPIView):
    """ ListView for Routines shared """
    queryset = ShareRoutineUser.objects.all()
    serializer_class = ShareRoutineUserSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAuthenticated, IsOccupant]

    def get_queryset(self):
        user = self.request.user
        return ShareRoutineUser.objects.filter(occupant=user)


class ShareRoutineUserDetail(generics.RetrieveDestroyAPIView):
    """ ListView for the deatil of a Routine shared """
    queryset = ShareRoutineUser.objects.all()
    serializer_class = ShareRoutineUserDetailSerializer
    permission_classes = [IsAuthenticated, IsOccupant | IsAuthenticated, IsOwner]


class ShareRoutinePublicCreate(generics.CreateAPIView):
    """ View to create the public routine """
    queryset = ShareRoutinePublic.objects.all()
    serializer_class = ShareRoutinePublicSerializer
    permission_classes = [IsAuthenticated]


class ShareRoutinePublicDetail(generics.RetrieveDestroyAPIView):
    """ View to see the public routine """
    queryset = ShareRoutinePublic.objects.all()
    serializer_class = ShareRoutinePublicSerializer
    permission_classes = [ReadOnly | IsOwner]
