#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-14
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase

from authentication.models import User
from save.models import Favorites
from search.models import Product, Category


class TestModels(TestCase):
    """To test the save app models"""
    def setUpTestData():
        """Create a temp user and temp products to perform tests"""
        user = User.objects.create(email='remy@purbeurre.fr')

        Category.objects.create(name="Pate à tartiner")

        product_1 = Product.objects.create(
            name="Beurre de cacahuètes",
            category_id=Category.objects.get(name="Pate à tartiner"),
            store="Carrefour",
            nutriscore="c",
            barcode="012456870000",
            url="https://peanutbutter.fr",
            image="https://peanutbutter.fr/photo.jpg",
            lipids_for_100g="2.60",
            saturated_fats_for_100g="0.59",
            sugars_for_100g="0.11",
            salt_for_100g="3.51",
        )

        product_2 = Product.objects.create(
            name="Ovomaltine",
            category_id=Category.objects.get(name="Pate à tartiner"),
            store="Leclerc, BioCoop",
            nutriscore="a",
            barcode="0189654870000",
            url="https://ovomaltine.fr",
            image="https://ovomaltine.fr/photo.jpg",
            lipids_for_100g="4.59",
            saturated_fats_for_100g="0.02",
            sugars_for_100g="1.54",
            salt_for_100g="3.25",
        )

        Favorites.objects.create(
            original_product_id=product_1,
            substitute_id=product_2,
            user_id=user
        )

    def test_original_product_id(self):
        """To check the foreign key to the original product"""
        data = Favorites.objects.get(id=1)
        self.assertEqual(data.original_product_id.name, "Beurre de cacahuètes")

    def test_substitute_product_id(self):
        """To check the foreign key to the substitute"""
        data = Favorites.objects.get(id=1)
        self.assertEqual(data.substitute_id.nutriscore, "a")

    def test_related_user_id(self):
        """To check the foreign key to the substitute"""
        data = Favorites.objects.get(id=1)
        self.assertEqual(data.user_id.email, "remy@purbeurre.fr")
