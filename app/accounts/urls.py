from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import RegisterUser, UserProfile, UserProfileSearch, LoginView, ConfirmEmailView

router = DefaultRouter()
router.register(r'', UserProfileSearch, basename='usersearch')

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration_account'),
    path('login/', LoginView.as_view(), name='login'),
    path('<int:pk>/', UserProfile.as_view(), name='account_detail'),
    path('confirm-email/', ConfirmEmailView.as_view(), name='confirm_email_account')
]

urlpatterns += router.urls
