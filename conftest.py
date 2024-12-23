import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.common.utils import DBHandler as InitDB
from pathlib import Path
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from dataclasses import dataclass
from config.config import TEST_DB_NAME
from config.config import CHROME_DRIVER_PATH


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="not_selected",
        help="Specify the browser name - 'chrome' or 'firefox'",
    )


@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        return request.getfixturevalue("chrome_driver")
    elif browser == "firefox":
        return request.getfixturevalue("firefox_driver")
    else:
        raise ValueError(
            f"Browser is not set. Use --browser option via cmd or pytest.ini"
        )


@pytest.fixture(scope="module")
def pause():
    def _pause(seconds, stop=0):
        time.sleep(seconds)
        if stop:
            input("\nPRESS ANY KEY TO CONTINUE ...")

    return _pause


@pytest.fixture(scope="session")
def chrome_driver_path():
    return Path(__file__).parent / CHROME_DRIVER_PATH


@pytest.fixture(scope="session")
def get_db_path():
    return Path(__file__).parent / TEST_DB_NAME


@pytest.fixture(scope="session")
def init_database(get_db_path):
    db_path = get_db_path

    if not db_path.exists():
        print("\n---CREATE DATABASE FROM SCRATCH ---")
        InitDB.run_queries(
            db_path,
            [
                InitDB.CREATE_PRODUCTS_TBL_SQL,
                InitDB.FILL_PRODUCTS_TBL_SQL,
                InitDB.CREATE_CUSTOMERS_TBL_SQL,
                InitDB.FILL_CUSTOMERS_TBL_SQL,
                InitDB.CREATE_ORDERS_TBL_SQL,
                InitDB.FILL_ORDERS_TBL_SQL,
            ],
        )


@pytest.fixture
def db(init_database, get_db_path):
    db = Database(get_db_path)
    yield db
    db.close()


@pytest.fixture
def github_api():
    api = GitHub()

    yield api


@dataclass
class TestUser:
    owner: str = "dmytroPPK"
    repo: str = "GL-QAAUTO101"


@pytest.fixture
def test_user():
    return TestUser()


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Dmytro"
        self.second_name = "Prokopenko"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()
