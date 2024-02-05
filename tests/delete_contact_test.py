import unittest
import os
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
            cls.url = "http://localhost:80/badcrud"

    def test_xss(self):
        login_url = self.url + '/login.php'
        self.browser.get(login_url)
        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()

        self.browser.find_element(By.NAME, 'thing').send_keys('<script>alert("XSS Attack!");</script>')
        self.browser.find_element(By.NAME, 'submit').click()
        alert = self.browser.switch_to.alert
        self.assertEqual('XSS Attack!', alert.text)
        alert.accept()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
