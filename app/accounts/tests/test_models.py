from django.test import TestCase
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class ModelCustomUserTestCase(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            'worktion@gmail.com',
            'strongpass',
            'Workout',
            'Collection',
            'admin'
        )

        self.assertEqual(user.email, 'worktion@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        user = CustomUser.objects.create_superuser(
            'worktion@gmail.com',
            'strongpass',
            'Workout',
            'Collection',
            'admin'
        )

        self.assertEqual(user.email, 'worktion@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

