# #! /usr/bin/env python3
# # coding: utf-8

# """
# Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-15
# Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

# """

# from django.test import TestCase
# from unittest.mock import patch

# from search.models import Category, Product
# from search.management.commands.database import Database


# class TestDatabase(TestCase):
#     """To test the api request methods"""
#     def setUp()
#         self.api = Database()

#     @patch("search.management.commands.database.requests.get")
#     def test_database_properly_filled(self, mock_json):
#         mock_json.return_value.json.return_value = {
#             'products': [{
#                 'product_name_fr': 'Mock Produit 1',
#                 'stores': 'Magasin 1',
#                 'nutrition_grade_fr': ['a'],
#                 'code': '123456789',
#                 'image_url': 'https://image_produit_1.fr',
#                 'url': 'https://url_produit_1.fr',
#                 'nutriments': {
#                     'salt_100g': '1.1',
#                     'sugars_100g': '1.09',
#                     'fat_100g': '22.15',
#                     'saturated-fat_100g': '10.2',},
#                 },

#                 {
#                 'product_name_fr': 'Mock Produit 2',
#                 'stores': 'Magasin 2',
#                 'nutrition_grade_fr': ['a'],
#                 'code': '987654321',
#                 'image_url': 'https://image_produit_2.fr',
#                 'url': 'https://url_produit_2.fr',
#                 'nutriments': {
#                     'salt_100g': '1.1',
#                     'sugars_100g': '1.09',
#                     'fat_100g': '22.15',
#                     'saturated-fat_100g': '10.2',}
#                 },  
#             ]
#         }

