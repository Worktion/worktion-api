from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet

router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet, basename='exercise')

urlpatterns = router.urls
