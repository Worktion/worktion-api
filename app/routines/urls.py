from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    RoutineList,
    RoutineDetail,
    ExecutionBlockViewSet,
    ExecutionExerciseViewSet
)

routerBlocks = DefaultRouter()
routerBlocks.register(r'blocks', ExecutionBlockViewSet, basename='execution_blocks')
routerExercise = DefaultRouter()
routerExercise.register(
    r'execution_exercises',
    ExecutionExerciseViewSet,
    basename='execution_exercises'
)


urlpatterns = [
    path('routines/', RoutineList.as_view(), name='routine_list'),
    path('routines/<int:pk>/', RoutineDetail.as_view(), name='routine_detail'),
]

urlpatterns += routerBlocks.urls
urlpatterns += routerExercise.urls
