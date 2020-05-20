#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-15
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TransactionTestCase
from django.core.management import call_command

from search.models import Category, Product


class TestDbInit(TransactionTestCase):
    """To test the command which populates the database"""

    def test_insert_categories(self):
        """To check the categories number"""
        call_command("db_init")
        self.assertEqual(Category.objects.all().count(), 15)

    def test_insert_products(self):
        """To check that a certain amount of products are there"""
        call_command("db_init")
        self.assertEqual(Product.objects.all().count(), 3718)
