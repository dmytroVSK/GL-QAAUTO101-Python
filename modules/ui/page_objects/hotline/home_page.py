from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.hotline.place_ad_page import PlaceAdPage


class HomePage(BasePage):

    URL = "https://hotline.ua/ua"

    class Locators:
        SEARCH_INPUT = (By.XPATH, '//*[@id="autosuggest"]/div[1]/input')
        SEARCH_TITLE = (By.CLASS_NAME, "search__title")
        ELEMS_SEARCH_RESULT = (By.CLASS_NAME, "list-item__info")
        LINK_PLACE_AD_PAGE = (By.LINK_TEXT, "Розмістити рекламу")
        FOOTER = (By.TAG_NAME, "footer")

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def get_qnt_search_result(self, search_text: str):
        self.__search_input_fill_and_return(search_text)
        result_elems = self._find_elements_visible(self.Locators.ELEMS_SEARCH_RESULT)
        return len(result_elems)

    def check_title_search_contains(self, search_text: str):
        self.__search_input_fill_and_return(search_text)
        title_elem = self._find_element_dom(self.Locators.SEARCH_TITLE)
        return search_text in title_elem.text

    def __search_input_fill_and_return(self, search_text: str):
        search_elem = self._find_element_visible(self.Locators.SEARCH_INPUT)
        search_elem.clear()
        search_elem.send_keys(search_text + Keys.RETURN)

    def goto_place_ad_page(self):
        page_link = self._find_element_visible(self.Locators.LINK_PLACE_AD_PAGE)
        page_link.click()
        return PlaceAdPage(self.driver)
