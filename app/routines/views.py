from rest_framework import viewsets
from .serializers import RoutineSerializer
from .models import Routine


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
