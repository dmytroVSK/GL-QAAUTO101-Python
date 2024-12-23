import pytest
from modules.ui.page_objects.hotline.home_page import HomePage


@pytest.mark.ui
def test_check_title_of_search(driver):
    search_text = "oneplus 13"

    home_page = HomePage(driver)
    home_page.open()

    assert home_page.check_title_search_contains(search_text)


@pytest.mark.ui
def test_check_qnt_search(driver):
    search_text = "oneplus 13"

    home_page = HomePage(driver)
    home_page.open()

    assert home_page.get_qnt_search_result(search_text) > 0


@pytest.mark.ui
def test_open_place_ad_page(driver):
    title_to_check = "Розмістити рекламу | Hotline"
    home_page = HomePage(driver)
    home_page.open()
    place_ad_page = home_page.goto_place_ad_page()

    assert place_ad_page.check_title_is(title_to_check)
