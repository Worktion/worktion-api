import uuid
from django.db import models
from django.contrib.auth import get_user_model
from routines.models import Routine

User = get_user_model()


class ShareRoutineUser(models.Model):
    """ Model to share routine with others Users """
    routine = models.ForeignKey(
        Routine,
        related_name='share_routine_users',
        on_delete=models.PROTECT
    )
    owner = models.ForeignKey(
        User,
        related_name='owner_share_routine',
        on_delete=models.PROTECT
    )
    occupant = models.ForeignKey(
        User,
        related_name='occupant_share_routine',
        on_delete=models.PROTECT
    )


class ShareRoutinePublic(models.Model):
    """ Model to share routine with the public """
    routine = models.ForeignKey(
        Routine,
        related_name='share_routine_publics',
        on_delete=models.PROTECT
    )
    owner = models.ForeignKey(
        User,
        related_name='owner_share_routine_public',
        on_delete=models.PROTECT
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
