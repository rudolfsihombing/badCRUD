import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginEmpty(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Firefox(options=option)

    def test_login_empty(self):
        login_url = 'http://localhost:80/badcrud/login.php'
        response = requests.post(login_url, data={})
        self.assertIn('<form class="form-signin"', response.text)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
