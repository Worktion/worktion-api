from django.urls import path
from .views import (
    ShareRoutineUserList,
    ShareRoutineUserDetail,
    ShareRoutinePublicCreate,
    ShareRoutinePublicDetail,
    ShareRoutineUserOccupantList,
    ShareRoutineUserOccupantDelete,
    ShareRoutinePublicRetrieve,
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
        'share/routines/<int:pk>/occupants/',
        ShareRoutineUserOccupantList.as_view(),
        name='share_routine_occupants-list'
    ),
    path(
        'share/routines/<int:pk>/occupants/<int:occupant>/',
        ShareRoutineUserOccupantDelete.as_view(),
        name='share_routine_occupants-list'
    ),
    path(
        'share/public/',
        ShareRoutinePublicCreate.as_view(),
        name='share_public-create'
    ),
    path(
        'share/public/<uuid:pk>/',
        ShareRoutinePublicDetail.as_view(),
        name='share_public-detail'
    ),
    path(
        'share/public/routine/<int:pk>/',
        ShareRoutinePublicRetrieve.as_view(),
        name='share_public-detail'
    ),


]
