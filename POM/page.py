from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_link(self, url):
        self.driver.get(url)

    def verify_title(self):
        assert 'Yahoo' in self.driver.title  # Execute the assertion

    def search_on_yahoo(self, search_term):
        search_box = self.driver.find_element(By.NAME, 'p')  # Replace with the correct locator
        search_box.clear()
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        print('Search executed.')

        # Wait for the search results to load and verify the presence of an element on the results page
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@value='test']"))
            )

            
            print('Search results verified. Test passed.')
        except (TimeoutException, NoSuchElementException):
            print('Search results verification failed. Test failed.')
        except AssertionError:
            print('Title check failed. Test failed.')
        except Exception as e:
            print(f'An error occurred: {e}. Test failed.')
