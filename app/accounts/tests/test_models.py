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


class AuthenticationUserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            'worktion@gmail.com',
            'strongpass',
            'Workout',
            'Collection',
            'admin'
        )

    def test_login_user_bad_request(self):
        self.assertRaises(ValueError, CustomUser.objects.login, "", "")
        with self.assertRaises(ValueError) as cm:
            CustomUser.objects.login("swsw", "")
        exception = cm.exception
        self.assertEqual(str(exception), 'The password must be set')
        self.assertRaises(ValueError, CustomUser.objects.login, "", "")
        self.assertRaises(ValueError, CustomUser.objects.login, None, None)
        self.assertRaises(ValueError, CustomUser.objects.login, None, None)
        self.assertRaises(ValueError, CustomUser.objects.login, "cevvrgtcdcs", None)

    def test_login_user_bad_credentials(self):
        with self.assertRaises(ValueError)as ex:
            CustomUser.objects.login("cevvrgtcdcs", "xdccd")
        self.assertEqual(str(ex.exception), 'email not found')
        with self.assertRaises(ValueError)as ex:
            CustomUser.objects.login("worktion@gmail.com", "xdccd")
        self.assertEqual(str(ex.exception), 'User or password incorrect')
        with self.assertRaises(Exception)as ex:
            CustomUser.objects.login("worktion@gmail.com", "strongpass")
        self.assertEqual(str(ex.exception), 'email has not yet been verified')

    def test_login_user_good_credentials(self):
        self.user.validate_email()
        self.assertIsNotNone(CustomUser.objects.login("worktion@gmail.com", "strongpass"))
