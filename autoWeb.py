from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BrowserAutomation:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.browser = webdriver.Edge(service=self.service)

    def go_to_website(self, url, verbose=False):
        self.browser.get(url)
        if verbose:
            print(f"Navigated to {url}")
            print(f"Page title: {self.browser.title}")

    def get_div_by_class_name(self, class_name):
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name))
            )
            return element
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def from_div_get(self, div_element, tag_name, attribute=None, class_name=None):
        try:
            if class_name:
                element = div_element.find_element(By.CLASS_NAME, class_name)
            else:
                element = div_element.find_element(By.TAG_NAME, tag_name)

            if attribute:
                return element.get_attribute(attribute)
            else:
                return element.text
        except Exception as e:
            print(f"An error occurred while extracting data: {e}")
            return None

    def close_browser(self):
        self.browser.quit()

# Example usage
if __name__ == '__main__':
    driver_path = r"D:\Programs\edgedriver_win32\msedgedriver.exe"
    automation = BrowserAutomation(driver_path)
    automation.go_to_website('https://www.cardmarket.com/en/Magic/Users/Manamaze/Offers/Singles?name=Ledger+shredder&sortBy=price_asc')
    element = automation.get_div_by_class_name('article-row')
    print(automation.from_div_get(element, 'a', 'href'))
    if element:
        price = automation.from_div_get(element, 'span', None, 'price-container')
        print(f"Price: {price}")
    automation.close_browser()