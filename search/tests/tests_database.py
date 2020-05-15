#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-15
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase
from unittest.mock import patch

from search.models import Category, Product
from search.management.commands.database import Database


class TestDatabase(TestCase):
    """To test the api request methods"""
    def setUp()
