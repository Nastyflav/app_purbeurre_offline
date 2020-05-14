#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-14
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase, Client
from django.urls import reverse
from django.db import IntegrityError
from authentication.models import User


class TestModels(TestCase):
    """To test the authentication models"""
    def setUp(self):
        """ Create a temp user to perform tests"""
        self.client = Client()
        self.login_url = reverse('authentication:login')
        self.logout_url = reverse('authentication:logout')
        self.profile_url = reverse('authentication:profile')
        self.user = User.objects.create(email='user@test.dj')
        self.user.set_password('supertest2020')
        self.user.save()

    def test_signup_and_str_return_when_user_creation_is_ok(self):
        """Test when the creation of new user is authorized"""
        new_user_email = 'newuser@test.dj'
        user = User.objects.create(email=new_user_email)
        user.set_password('@supernouveau')
        user.save()

        user = User.objects.get(email=new_user_email)
        self.assertIsInstance(user, User)
        self.assertEqual(str(user), new_user_email)