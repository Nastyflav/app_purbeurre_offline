#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-14
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase

from authentication.forms import SignUpForm, LogInForm


class TestSignUpForm(TestCase):
    """To test the authentication form"""
    data = {
        'email': 'some@email.com',
        'password1': 'some password',
        'password2': 'some password',
    }

    def test_valid_form(self):
        """To test if all the required fields are there"""
        self.form = SignUpForm(self.data)
        self.assertTrue(self.form.is_valid())

    def test_if_invalid_email(self):
        """To test when an incorrect email is given"""
        self.new_data = self.data.copy()
        self.new_data['email'] = 'no arobase email'
        self.form = SignUpForm(self.new_data)
        self.assertFalse(self.form.is_valid())

    def test_when_missing_required_fields(self):
        """To check the response when a required fields is missing"""
        for field in ('email', 'password1', 'password2'):
            with self.subTest(field=field):
                my_data = self.data.copy()
                my_data[field] = ''
                form = SignUpForm(my_data)
                self.assertFalse(form.is_valid())

    def test_password_safe_input(self):
        """
        To check the safety of the system
        password1 must equals password2

        """
        self.form = SignUpForm()
        input_type = self.form['password1'].field.widget.input_type
        self.assertEqual(input_type, 'password')
        input_type = self.form['password2'].field.widget.input_type
        self.assertEqual(input_type, 'password')


class TestLogInForm(TestCase):
    """To test the login form"""
    data = {
        'username': 'some@email.com',
        'password': 'some password',
    }

    def test_if_invalid_email(self):
        """To test when an incorrect email is given"""
        self.new_data = self.data.copy()
        self.new_data['username'] = 'wrong@email.com'
        self.form = LogInForm(self.new_data)
        self.assertFalse(self.form.is_valid())

    def test_if_invalid_password(self):
        """To test when an incorrect password is given"""
        self.new_data = self.data.copy()
        self.new_data['password'] = 'wrong password'
        self.form = LogInForm(self.new_data)
        self.assertFalse(self.form.is_valid())

    def test_when_missing_required_fields(self):
        """To check the response when a required fields is missing"""
        for field in ('username', 'password'):
            with self.subTest(field=field):
                my_data = self.data.copy()
                my_data[field] = ''
                form = LogInForm(my_data)
                self.assertFalse(form.is_valid())
