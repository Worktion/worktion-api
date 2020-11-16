from rest_framework import viewsets, permissions
from .models import Exercise
from .serializers import ExerciseSerializer


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    """
    Permission for for the administrator to be the only
    one who can administer the exercises
    """
    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly,
            self).has_permission(request, view)

        return request.method in permissions.SAFE_METHODS or is_admin


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    View of the exercise
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAdminUserOrReadOnly
    ]
