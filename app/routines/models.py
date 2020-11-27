from django.db import models
from django.contrib.auth import get_user_model
from exercises.models import Exercise

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


class ExecutionBlock(models.Model):
    """ Model to wrap the set of execution exercise """
    routine = models.ForeignKey(
        Routine,
        related_name='blocks_routine',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)


class ExecutionExercise(models.Model):
    """ Model for the execution of a exercise """
    TYPE_EXECUTION = (
        ('secs', 'Seconds'),
        ('reps', 'Repetitions')
    )
    execution_block = models.ForeignKey(
        ExecutionBlock,
        related_name='executions_block',
        on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(
        Exercise,
        related_name='execution_exercise',
        on_delete=models.PROTECT
    )
    quantity = models.IntegerField()
    typeExecution = models.CharField(max_length=11, choices=TYPE_EXECUTION)
