from django.contrib.auth import get_user_model
from django.test import TestCase


class NewUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
                username='julien',
                email='julien@jul1en.com',
                password='TestPass123'
        )
        self.assertEqual(user.username, 'julien')
        self.assertEqual(user.email, 'julien@jul1en.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
                username='wonderfuladmin',
                email='wonderful@jul1en.com',
                password='TestPass123'
        )
        self.assertEqual(admin_user.username, 'wonderfuladmin')
        self.assertEqual(admin_user.email, 'wonderful@jul1en.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

