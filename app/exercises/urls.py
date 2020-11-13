from django.urls import path
from .views import ExerciseList

urlpatterns = [
    path('', ExerciseList.as_view(), name='exercises_list'),
]