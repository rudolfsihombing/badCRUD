import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SQLInjectionTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        cls.browser = webdriver.Firefox(options=option)
        try:
            cls.url = os.environ['URL']
        except:
            cls.url = "http://localhost:80/badcrud"

    def test_edit_contact(self):
        login_url = self.url + '/login.php'
        self.browser.get(login_url)
        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin" OR 1=1--"')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('hello')
        self.browser.find_element(By.TAG_NAME, 'button').click()

        expected_result = self.browser.title
        actual_result = "Dashboard"
        self.assertIn(expected_result, actual_result)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')