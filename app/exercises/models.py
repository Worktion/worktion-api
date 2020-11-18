from django.db import models


class Exercise(models.Model):
    """ Model exercise """
    DIFFICULTIES = (
        ('novice', 'Novice'),
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('legendary', 'Legendary'),
    )
    name = models.CharField(max_length=60)
    similar_names = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    dificulty = models.CharField(max_length=15, choices=DIFFICULTIES)


class ExerciseImage(models.Model):
    """ Model for the exercise images """
    exercise = models.ForeignKey(Exercise, related_name='exercise_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="exercise-images")
