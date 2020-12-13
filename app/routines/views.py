from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission
from .serializers import (
    RoutineSerializer,
    OnlyRoutineSerializer,
    ExecutionBlockSerializer,
    ExecutionExerciseSerializer
)
from .models import Routine, ExecutionBlock, ExecutionExercise


class IsOwner(BasePermission):
    """
    Object-level permission to only allow owners
    get and edit his routines
    """
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id


class IsOwnerBlocks(BasePermission):
    """
    Object-level permission to only allow owners
    get and edit his blocks of routines
    """
    def has_object_permission(self, request, view, obj):
        return obj.routine.user.id == request.user.id


class IsOwnerExercise(BasePermission):
    """
    Object-level permission to only allow owners
    get and edit his exercise of a block
    """
    def has_object_permission(self, request, view, obj):
        return obj.execution_block.routine.user.id == request.user.id


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


class ExecutionBlockViewSet(viewsets.ModelViewSet):
    """ Endpoint to create, update or delete a Block of exercises """
    queryset = ExecutionBlock.objects.all()
    serializer_class = ExecutionBlockSerializer
    permission_classes = [IsAuthenticated, IsOwnerBlocks]


class ExecutionExerciseViewSet(viewsets.ModelViewSet):
    """ Endpoint to create update or delete a execution of exercises """
    queryset = ExecutionExercise.objects.all()
    serializer_class = ExecutionExerciseSerializer
    permission_classes = [IsAuthenticated, IsOwnerExercise]
