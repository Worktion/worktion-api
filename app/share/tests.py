from django.test import TestCase
from share.models import ShareRoutineUser
from routines.models import Routine
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class ModelShareRoutineUserTestCase(TestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(
            'worktion@gmail.com',
            'strongpass',
            'Workout',
            'Collection',
            'admin'
        )
        self.user2 = CustomUser.objects.create_user(
            'user2@gmail.com',
            'strongpass',
            'Workout',
            'Collection',
            'admin'
        )
        self.routine = Routine.objects.create(
            user=self.user1,
            name="Routine1",
            is_public=False,
            time=30,
            dificulty="novice",
            muscle_group="fullbody"
        )

    def test_share_routine(self):
        print(self.routine.name)
        share = ShareRoutineUser.objects.create(
            routine=self.routine,
            owner=self.user1,
            occupant=self.user2,
        )

        self.assertEqual(share.owner.id, self.user1.id)
