from django.db import models

# Create your models here.

class Exercise(models.Model):
    DIFFICULTIES = (
        ('S','Student'),
        ('B','Beginner'),
        ('I','Intermediate'),
        ('A','Advanced'),
        ('L','Legendary'),
    )
    name = models.CharField(max_length=60)
    similar_names = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    dificulty = models.CharField(max_length=1, choices=DIFFICULTIES)


class ExerciseImage(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="exercise-images")
    #thumbnail = models.ImageField(upload_to="exercise-thumbnails", null=True)
