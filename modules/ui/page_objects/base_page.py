from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:

    TIMEOUT = 5

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()

    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        self._wait().until(
            lambda driver: element.is_displayed() and element.is_enabled()
        )
        self._scroll_to_element(element)
        return element

    def find_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        elements_are_ready = lambda elems: all(
            elem.is_displayed and elem.is_enabled() for elem in elems
        )
        self._wait().until(lambda driver: elements_are_ready(elements))
        return elements

    def _wait(self, timeout=TIMEOUT):
        return Wait(self.driver, timeout)

    def _scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
