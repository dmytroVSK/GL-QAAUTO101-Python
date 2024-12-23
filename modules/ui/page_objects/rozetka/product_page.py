from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage


class ProductPage(BasePage):
    URL = ""

    class Locators:
        PRODUCT_NAME = (By.CSS_SELECTOR, "h1.title__font")
        BUY_BUTTON = (By.CSS_SELECTOR, "button.buy-button")
        CONTINUE_SHOPPING_BUTTON = (
            By.CSS_SELECTOR,
            'button[data-testid="continue-shopping-link"]',
        )
        CART_BUTTON = (By.CLASS_NAME, "header-cart__button")
        CART_PRODUCT_TITLES = (By.CSS_SELECTOR, "span.cart-product__title")

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def get_item_name(self):
        element = self._find_element_visible(self.Locators.PRODUCT_NAME)
        return element.text

    def add_to_cart(self):
        self._click_buy_btn()
        self._click_continue_shopping_btn()

    def check_cart(self, item_name: str):
        self._click_cart_btn()
        product_titles = self._find_elements_visible(self.Locators.CART_PRODUCT_TITLES)
        return (
            False
            if len(product_titles) == 0
            else self._item_in_list(item_name, product_titles)
        )

    def _click_buy_btn(self):
        self._find_element_visible(self.Locators.BUY_BUTTON).click()

    def _click_continue_shopping_btn(self):
        self._find_element_visible(self.Locators.CONTINUE_SHOPPING_BUTTON).click()

    def _click_cart_btn(self):
        element = self._find_element_visible(self.Locators.CART_BUTTON)
        # google account iframe overlap button
        self.driver.execute_script("arguments[0].click();", element)

    def _item_in_list(self, item_name: str, titles_list):
        return any([item_name in title.text for title in titles_list])
