from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Routine(models.Model):
    """ Routine model """
    DIFFICULTIES = (
        ('novice', 'Novice'),
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('legendary', 'Legendary'),
    )
    MUSCLE_GROUPS = (
        ('fullbody', 'Full Body'),
        ('chest', 'Chest'),
        ('legs', 'Legs'),
        ('arm', 'Arm'),
        ('back', 'Back'),
        ('shoulder', 'Shoulder'),
    )
    user = models.ForeignKey(
        User,
        related_name='routines_user',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    time = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dificulty = models.CharField(max_length=15, choices=DIFFICULTIES)
    muscle_group = models.CharField(max_length=10, choices=MUSCLE_GROUPS)
    cover = models.ImageField(upload_to='routine-images')
