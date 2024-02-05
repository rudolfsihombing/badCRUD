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
        cls.name_query = ''.join(random.choices(string.ascii_letters, k=10))

    def test_create_contact(self):
        login_url = self.url + '/login.php'
        self.browser.get(login_url)
        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()
        
        create_url = self.url + '/create.php'
        self.browser.get(create_url)

        self.browser.find_element(By.ID, 'name').send_keys(self.name_query)
        self.browser.find_element(By.ID, 'email').send_keys('test@example.com')
        self.browser.find_element(By.ID, 'phone').send_keys('1234567890')
        self.browser.find_element(By.ID, 'title').send_keys('Developer')

        self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        index_page_title = "Dashboard"
        actual_title = self.browser.title
        self.assertEqual(index_page_title, actual_title)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
