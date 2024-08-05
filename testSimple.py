from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize the Chrome WebDriver
browser = webdriver.Chrome()

try:
    # Navigate to Yahoo
    browser.get('http://www.yahoo.com')
    
    # Check that 'Yahoo' is in the page title
    assert 'Yahoo' in browser.title
    print('Title check passed.')

    # Find the search box and perform a search
    elem = browser.find_element(By.NAME, 'p')  # Find the search box
    elem.send_keys('seleniumhq' + Keys.RETURN)
    print('Search executed.')

    # Wait for the search results to load and verify the presence of an element on the results page
    try:
        # Wait up to 10 seconds for an element containing 'Selenium' in its text to appear
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Selenium')]"))
        )
        print('Search results verified. Test passed.')
    except TimeoutException:
        print('Search results verification failed. Test failed.')
    except NoSuchElementException:
        print('Element not found in the search results. Test failed.')

except AssertionError:
    print('Title check failed. Test failed.')

except Exception as e:
    print(f'An error occurred: {e}. Test failed.')

finally:
    # Close the browser
    browser.quit()
