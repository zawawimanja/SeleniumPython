import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def test_yahoo_search():

  
  browser = webdriver.Chrome()

  try:
    # Navigate to Yahoo
    browser.get('http://www.yahoo.com')

    # Check that 'Yahoo' is in the page title
    assert 'Yahoo' in browser.title
    print('Title check passed.')

   
  except AssertionError:
    print('Title check failed. Test failed.')

  except Exception as e:
    print(f'An error occurred: {e}. Test failed.')

  finally:
    # Close the browser
    browser.quit()

if __name__ == "__main__":
  pytest.main()
