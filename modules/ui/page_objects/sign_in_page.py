from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):

    URL = "https://github.com/login"

    LOGIN_ELEMENT = (By.ID, "login_field")
    PASSWORD_ELEMENT = (By.ID, "password")
    BUTTON_ELEMENT = (By.NAME, "commit")
    FOOTER_LINKS = (By.CSS_SELECTOR, "li.mx-2")

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def try_login(self, username, password):
        login_element = self._find_element_visible(self.LOGIN_ELEMENT)
        login_element.send_keys(username)

        password_element = self._find_element_visible(self.PASSWORD_ELEMENT)
        password_element.send_keys(password)

        button_element = self._find_element_visible(self.BUTTON_ELEMENT)
        button_element.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def check_link_qnt_footer(self, expected_link_qnt):
        return len(self._find_elements_visible(self.FOOTER_LINKS)) == expected_link_qnt
