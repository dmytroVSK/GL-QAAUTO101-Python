import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


@pytest.mark.skip(reason="use driver manager")
@pytest.mark.ui
def test_try_open_login_page(chrome_driver_path):
    """test with manual linked binary"""
    driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path))

    driver.get("https://github.com/login")

    driver.close()


@pytest.mark.ui
def test_check_incorrect_username(driver, pause):
    driver.get("https://github.com/login")

    login_input = driver.find_element(By.ID, "login_field")
    login_input.send_keys("bober123@nomail.com")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Opps123!!!")

    signin_button = driver.find_element(By.NAME, "commit")
    signin_button.click()

    assert driver.title == "Sign in to GitHub · GitHub"
