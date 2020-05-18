#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-05-15
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class TestChrome(LiveServerTestCase):
    """To test a user story using Chrome"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        """Test when the user wants to log in"""
        self.selenium.get('%s%s' % (self.live_server_url, '/authentication/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('selenium@user.test')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('test2020')
        submit = self.selenium.find_element_by_id("submit-button")
        submit.send_keys(Keys.RETURN)

    def test_search_product_details(self):
        """To test when the user wants to search a prod and its details"""
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        query_input = self.selenium.find_element_by_id("query")
        query_input.send_keys('nutella')
        search = self.selenium.find_element_by_id("search-btn")
        search.send_keys(Keys.RETURN)
        product=self.selenium.find_element_by_xpath("//input[@id='details-link']")[0]
        product.click()

