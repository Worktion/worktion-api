from django.test import TestCase
from exercises.models import Exercise


class ModelExerciseTestCase(TestCase):
    def test_create_exercise(self):
        exercise = Exercise.objects.create(
            name='test',
            similar_names='test2',
            description='test descrip',
            dificulty='beginner'
        )
        self.assertEqual(exercise.name, 'test')
        self.assertEqual(exercise.similar_names, 'test2')
