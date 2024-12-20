import pytest
from modules.api.clients.github import GitHub
from dataclasses import dataclass


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
