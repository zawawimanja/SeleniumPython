import pytest
from selenium import webdriver
from page import Page  # Assuming Page class is in page_objects directory


@pytest.fixture
def driver():
    """Fixture to provide a WebDriver instance"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_yahoo_and_verify_title(driver):
    """Test case using POM and pytest"""
    page = Page(driver)
    page.open_link("https://www.yahoo.com")
    page.verify_title()