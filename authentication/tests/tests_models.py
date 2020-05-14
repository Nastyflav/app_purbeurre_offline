#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-14
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase
from django.db import IntegrityError

from authentication.models import User


class TestModels(TestCase):
    """To test the authentication models"""
    def setUp(self):
        """ Create a temp user to perform tests"""
        self.user = User.objects.create(
            email='user@test.dj', first_name='User', last_name='Django')
        self.user.set_password('supertest2020')

    def test_first_name_max_length(self):
        """To check the first name lenght"""
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 40)

    def test_last_name_max_length(self):
        """To check the last name lenght"""
        user = User.objects.get(id=2)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 40)

    def test_signup_and_str_return_when_user_creation_is_ok(self):
        """Test when the creation of new user is authorized"""
        new_user_email = 'newuser@test.dj'
        user = User.objects.create(email=new_user_email)
        user.set_password('@supernouveau')
        user.save()

        user = User.objects.get(email=new_user_email)
        self.assertIsInstance(user, User)
        self.assertEqual(str(user), new_user_email)

    def test_signup_when_user_already_exists(self):
        """Check if a similar user or a similar password already exists"""
        try:
            user = User.objects.create(email='user@test.dj')
            user.set_password('supernouveau')
            user.save()
        except IntegrityError:
            user = False
        self.assertFalse(user)
