#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-21
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase, Client
from django.urls import reverse
from django.db import IntegrityError
from authentication.models import User


class TestAuthentication(TestCase):
    """To test the authentication app"""
    def setUp(self):
        """ Create a temp user to perform tests"""
        self.client = Client()
        self.signup_url = reverse('authentication:signup')
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

    def test_signup_is_a_valid_action(self):
        """To check the redirection when the account creation is accepted"""
        response = self.client.post(self.signup_url, {
            'email': 'newuser@test.dj',
            'password1': 'supernouveau',
            'password2': 'supernouveau'
        })
        self.assertRedirects(
            response, '/', status_code=302, target_status_code=200)

    def test_signup_form_is_not_valid(self):
        """To check if the user can retry to sign up if he fails once"""
        response = self.client.post(self.signup_url, {
            'email': 'newuser',
            'password1': 'supernouveau',
            'password2': 'supernouveau1'
        })
        self.assertEqual(response.status_code, 200)

    def test_signup_when_user_already_exists(self):
        """Check if a similar user or a similar password already exists"""
        try:
            user = User.objects.create(email='user@test.dj')
            user.set_password('supernouveau')
            user.save()
        except IntegrityError:
            user = False
        self.assertFalse(user)
