import pytest
from modules.ui.page_objects.sign_in_page import SignInPage


@pytest.mark.ui
def test_check_incorrect_username_page_object(driver):
    sign_in_page = SignInPage(driver)
    sign_in_page.open()
    sign_in_page.try_login("booba", "booba123@invalid_email.com")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_link_qnt_on_footer(driver):
    sign_in_page = SignInPage(driver)
    sign_in_page.open()

    assert sign_in_page.check_link_qnt_footer(6)
