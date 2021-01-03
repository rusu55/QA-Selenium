import time
import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='../browser_drivers/chromedriver.exe')
        self.driver.get("http://hrm-online.portnov.com/")

    def test_valid_login(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id('btnLogin').click()

        time.sleep(3)
        welcome_text = driver.find_element_by_id('welcome').text
        self.assertEqual('Welcome Admin', welcome_text)

    def test_invalid_password_login(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password1')
        driver.find_element_by_id('btnLogin').click()

        time.sleep(3)
        warning_text = driver.find_element_by_id('spanMessage').text
        self.assertEqual('Invalid credentials', warning_text)

if __name__ == '__main__':
    unittest.main()
