#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-15
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase
from unittest.mock import patch
from django.core.management import call_command

from search.models import Product


def mock_api_request(*args, **kwargs):
    """Mock an API request from database.py"""
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({
            'products': [{
                'product_name_fr': 'Mock Produit 1',
                'stores': 'Magasin 1',
                'nutrition_grade_fr': 'a',
                'nutriscore_grade': 'a',
                'code': '123456789',
                'image_url': 'https://image_produit_1.fr',
                'url': 'https://url_produit_1.fr',
                'nutriments': {
                    'salt_100g': '1.1',
                    'sugars_100g': '1.09',
                    'fat_100g': '22.15',
                    'saturated-fat_100g': '10.2'},
                },

                {
                'product_name_fr': 'Mock Produit 2',
                'stores': 'Magasin 2',
                'nutrition_grade_fr': 'a',
                'nutriscore_grade': 'a',
                'code': '987654321',
                'image_url': 'https://image_produit_2.fr',
                'url': 'https://url_produit_2.fr',
                'nutriments': {
                    'salt_100g': '1.1',
                    'sugars_100g': '1.09',
                    'fat_100g': '22.15',
                    'saturated-fat_100g': '10.2'}
                },
            ]
        }, 200)


class TestDatabase(TestCase):
    """To test the api request methods"""
    @patch("requests.get", side_effect=mock_api_request)
    def test_request_api(self, mock_json):
        call_command("db_init")
        self.assertEqual(Product.objects.all().count(), 2)
