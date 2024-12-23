from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage


class PlaceAdPage(BasePage):

    URL = "https://hotline.ua/place-ad/"

    class Locators:
        pass

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def check_title_is(self, title: str):
        return title in self.driver.title
