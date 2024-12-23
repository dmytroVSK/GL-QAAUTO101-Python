import pytest
from conftest import pause
from modules.ui.page_objects.rozetka.home_page import HomePage


@pytest.mark.ui
def test_add_item_to_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    product_page = home_page.search_random_item()

    item_name = product_page.get_item_name()
    product_page.add_to_cart()

    assert product_page.check_cart(item_name)
