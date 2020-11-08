from django.urls import path
from .views import RegisterUser

urlpatterns = [
    path('registration/', RegisterUser.as_view()),
]