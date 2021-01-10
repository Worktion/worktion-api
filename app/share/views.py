from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, BasePermission
from .serializers import (
    ShareRoutineUserSerializer,
    ShareRoutinePublicSerializer,
    ShareRoutineUserDetailSerializer,
    ShareRoutineUserOccupantSerializer,
)
from .models import ShareRoutineUser, ShareRoutinePublic
from rest_framework.response import Response
from rest_framework import viewsets, status


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
    permission_classes = [IsOccupant | IsOwner]


class ShareRoutineUserOccupantList(generics.ListAPIView):
    """ List the occupant of a routine """
    queryset = ShareRoutineUser.objects.all()
    serializer_class = ShareRoutineUserOccupantSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return ShareRoutineUser.objects.filter(routine=self.kwargs['pk'])


class ShareRoutineUserOccupantDelete(generics.DestroyAPIView):
    """ Delete the occupant of a routine """
    queryset = ShareRoutineUser.objects.all()
    serializer_class = ShareRoutineUserOccupantSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def destroy(self, request, *args, **kwargs):
        exist = ShareRoutineUser.objects.filter(
            routine=self.kwargs['pk'],
            occupant=self.kwargs['occupant']
        ).exists()
        if not exist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        instance = ShareRoutineUser.objects.get(
            routine=self.kwargs['pk'],
            occupant=self.kwargs['occupant']
        )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class ShareRoutinePublicRetrieve(generics.RetrieveDestroyAPIView):
    """ View to see the public routine """
    queryset = ShareRoutinePublic.objects.all()
    serializer_class = ShareRoutinePublicSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def retrieve(self, request, *args, **kwargs):
        exist = ShareRoutinePublic.objects.filter(
            routine=self.kwargs['pk']
        ).exists()
        if not exist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance = ShareRoutinePublic.objects.get(routine=self.kwargs['pk'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
