import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.common.utils import DBHandler as InitDB
from dataclasses import dataclass
from config.config import TEST_DB_NAME
from pathlib import Path



@dataclass
class TestUser:
    owner: str = 'dmytroPPK'
    repo: str = 'GL-QAAUTO101'


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


@pytest.fixture
def github_api():
    api = GitHub()
    
    yield api


@pytest.fixture
def test_user():
    return TestUser()


# Database

@pytest.fixture(scope="session")
def get_db_path():
    return Path(__file__).parent / TEST_DB_NAME


@pytest.fixture(scope='session')
def init_database(get_db_path):
    db_path = get_db_path

    if not db_path.exists():
        print("\n---CREATE DATABASE FROM SCRATCH ---")
        InitDB.run_queries(db_path, [
            InitDB.CREATE_PRODUCTS_TBL_SQL,
            InitDB.FILL_PRODUCTS_TBL_SQL,
            InitDB.CREATE_CUSTOMERS_TBL_SQL,
            InitDB.FILL_CUSTOMERS_TBL_SQL,
            InitDB.CREATE_ORDERS_TBL_SQL,
            InitDB.FILL_ORDERS_TBL_SQL
        ])


@pytest.fixture
def db(init_database,get_db_path):
    db = Database(get_db_path)
    yield db
    db.close()
