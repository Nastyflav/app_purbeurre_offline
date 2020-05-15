#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-14
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase

from search.models import Category, Product


class TestModels(TestCase):
    """To test the save app models"""
    def setUpTestData():
        """Create a temp category and a temp product to perform tests"""
        Category.objects.create(name="Pate à tartiner")

        Product.objects.create(
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

    def test_category_max_length(self):
        """To check the category maximal lenght"""
        data = Category.objects.get(id=1)
        max_length = data._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_category_verbose_name(self):
        """To check the category verbose name"""
        data = Category.objects.get(id=1)
        verbose_name = data._meta.get_field('name').verbose_name
        self.assertEquals(verbose_name, "Nom")

    def test_category_str_method(self):
        """To check the category name is returned by the model"""
        data = Category.objects.get(id=1)
        self.assertEqual(str(data), data.name)

    def test_product_category_id(self):
        """To check the foreign key to the category"""
        data = Product.objects.get(id=1)
        self.assertEqual(data.category_id.name, "Pate à tartiner")

    def test_product_max_length(self):
        """To check the product fields max lenght"""
        data = Product.objects.get(id=1)
        name_max_length = data._meta.get_field('name').max_length
        self.assertEquals(name_max_length, 300)

    def test_product_verbose_name(self):
        """To check the product fields verbose names"""
        data = Product.objects.get(id=1)
        verbose_name = data._meta.get_field('store').verbose_name
        self.assertEquals(verbose_name, "Magasin(s)")

    def test_product_max_digits(self):
        """To check the product nutriments max digits"""
        data = Product.objects.get(id=1)
        max_digits = data._meta.get_field('lipids_for_100g').max_digits
        self.assertEquals(max_digits, 4)

    def test_product_decimal_places(self):
        """To check the product nutriments decimals"""
        data = Product.objects.get(id=1)
        decimals = data._meta.get_field('salt_for_100g').decimal_places
        self.assertEquals(decimals, 2)

    def test_product_str_method(self):
        """To check the product name is returned by the model"""
        data = Product.objects.get(id=1)
        self.assertEqual(str(data), data.name)
