from selenium import webdriver


class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_link(self, url):
        self.driver.get(url)

    def verify_title(self):
        assert 'Yahoo' in self.driver.title  # Execute the assertion
