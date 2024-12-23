from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    # TIMEOUT = 5

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.timeout = 5

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()

    def _wait(self):
        return Wait(self.driver, self.timeout)

    def _find_element_visible(self, locator, to_scroll=False):
        element = self._wait().until(EC.visibility_of_element_located(locator))
        if to_scroll:
            self._scroll_to_element(element)
        return element

    def _find_element_dom(self, locator):
        element = self._wait().until(EC.presence_of_element_located(locator))
        return element

    def _find_elements_visible(self, locator):
        elements = self._wait().until(EC.visibility_of_all_elements_located(locator))
        return elements

    def _find_elements_dom(self, locator):
        elements = self._wait().until(EC.presence_of_all_elements_located(locator))
        return elements

    def _scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
