from django.urls import path
from .views import RegisterUser, UserList

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration_account'),
    path('', UserList.as_view()),
]