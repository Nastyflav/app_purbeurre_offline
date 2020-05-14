#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-14
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase, Client
from django.urls import reverse


class TestUrls(TestCase):
    """To test the authentication urls file"""
    def setUp(self):
        """ Create a temp user to perform tests"""
        self.client = Client()
        self.login_url = reverse('authentication:login')
        self.logout_url = reverse('authentication:logout')
        self.signup_url = reverse('authentication:signup')
        self.profile_url = reverse('authentication:profile')

    def test_login_page_returns_200(self):
        """To test the status code and the login page"""
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertEqual(response.status_code, 200)

    def test_logout_redirection(self):
        """To test the redirection when the user logs out"""
        response = self.client.get(self.logout_url)
        self.assertRedirects(
            response, '/', status_code=302, target_status_code=200)

    def test_signup_page_returns_200(self):
        """To test the status code and the login page"""
        response = self.client.get(self.signup_url)
        self.assertTemplateUsed(response, 'registration/account_creation.html')
        self.assertEqual(response.status_code, 200)

    def test_profile_page_returns_200(self):
        """To test the status code and the profile page"""
        response = self.client.get(self.profile_url)
        self.assertTemplateUsed(response, 'registration/user_profile.html')
        self.assertEqual(response.status_code, 200)
