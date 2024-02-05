import unittest
import os
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CreateContactTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Firefox(options=option)
        try:
            cls.url = os.environ['URL']
        except:
            cls.url = "http://localhost"

    def test_edit_contact(self):
        login_url = self.url + '/login.php'
        self.browser.get(login_url)
        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()

        actions_section = self.browser.find_element(By.XPATH, "//tr[@role='row'][2]//td[contains(@class, 'actions')]")
        update_button = actions_section.find_element(By.XPATH, ".//a[contains(@class, 'btn-success')]")

        update_button.click()

        self.browser.find_element(By.ID, 'name').clear()
        self.browser.find_element(By.ID, 'name').send_keys("Harry Potter")

        self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        index_page_title = "Dashboard"
        actual_title = self.browser.title
        self.assertEqual(index_page_title, actual_title)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')