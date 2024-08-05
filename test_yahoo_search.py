from selenium import webdriver

class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_link(self, url):
        self.driver.get(url)

    def verify_title(self):
        assert 'Yahoo' in self.driver.title  # Execute the assertion
  

def open_link_with_pom(url):
    driver = webdriver.Chrome()
    page = Page(driver)
    page.open_link(url)
    page.verify_title
    
    driver.quit()

if __name__ == "__main__":
    link = "https://www.yahoo.com"
    open_link_with_pom(link)
