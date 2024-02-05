import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class TitleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Firefox(options=option)
        try:
            cls.url = os.environ['URL']
        except:
            cls.url = "http://localhost"

    def test(self):
        self.test_title_check()

    def test_title_check(self):
        login_url = self.url + '/login.php'
        self.browser.get(login_url)
        
        expected_result = "Login"        
        actual_result = self.browser.title
        self.assertIn(expected_result, actual_result)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()  


