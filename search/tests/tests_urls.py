#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-14
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
    """To test the search app urls file"""
    @classmethod
    def setUpTestData(cls):
        cls.search_url = reverse('search:search')
        cls.details_url = reverse('search:product-details', args=[1])

    def test_search_page_url(self):
        """To check the search url when requested"""
        self.assertEqual(self.search_url, '/search/')

    def test_details_page_url(self):
        """To test the url when product details are requested"""
        self.assertEqual(self.details_url, '/search/details/1')
