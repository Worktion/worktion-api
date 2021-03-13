from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import RegisterUser, UserProfile, UserProfileSearch, LoginView, ConfirmEmailView

router = DefaultRouter()
router.register(r'', UserProfileSearch, basename='usersearch')

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration_account'),
    path('login/', LoginView.as_view(), name='login_account'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh_token_account'),
    path('<int:pk>/', UserProfile.as_view(), name='account_detail'),
    path('confirm-email/', ConfirmEmailView.as_view(), name='confirm_email_account'),
]

urlpatterns += router.urls
