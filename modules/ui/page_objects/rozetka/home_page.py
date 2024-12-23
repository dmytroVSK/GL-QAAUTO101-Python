import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.rozetka.product_page import ProductPage


class HomePage(BasePage):

    URL = "https://rozetka.com.ua/ua/"

    class Locators:
        HOT_PRODUCTS = (By.TAG_NAME, "rz-product-tile")

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def search_random_item(self):
        hot_products = self._find_elements_visible(self.Locators.HOT_PRODUCTS)

        random_index = random.randint(0, len(hot_products) - 1)

        product = hot_products[random_index]

        product.click()

        return ProductPage(self.driver, self.driver.current_url)
