from django.urls import path
from .views import RegisterUser, UserList, UserProfile

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration_account'),
    path('', UserList.as_view()),
    path('<int:pk>/', UserProfile.as_view(), name='account_detail'),
]
