import time
import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_page_title(self):
        self.browser.get('http://www.yahoo.com')
        self.assertIn('Yahoo', self.browser.title)
        time.sleep(5)  # Keep the browser open for 5 seconds

if __name__ == '__main__':
    unittest.main(verbosity=2)
