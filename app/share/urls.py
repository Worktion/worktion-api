from django.urls import path
from .views import (
    ShareRoutineUserList,
    ShareRoutineUserDetail,
    ShareRoutinePublicDetail,
)

urlpatterns = [
    path(
        'share/routines/',
        ShareRoutineUserList.as_view(),
        name='share_routine'
    ),
    path(
        'share/routines/<int:pk>/',
        ShareRoutineUserDetail.as_view(),
        name='share_routine-detail'
    ),
    path(
        'share/public/<uuid:pk>/',
        ShareRoutinePublicDetail.as_view(),
        name='share_public-detail'
    ),

]
