from rest_framework.routers import DefaultRouter
from .views import RoutineList, RoutineDetail
from django.urls import path


urlpatterns = [
    path('routines/', RoutineList.as_view(), name='routine_list'),
    path('routines/<int:pk>/', RoutineDetail.as_view(), name='routine_detail'),
]
