import pytest
from app.config import Config


@pytest.fixture
def get_form_url() -> str:
    return f'http://{Config.SERVER_NAME}/get_form'


@pytest.fixture
def request_data() -> dict:
    return {
        "name": "John Doe",
        "email": "john_doe@email.com",
        "phone": "+7 012 345 67 89",
        "date_of_birth": "2000-01-01"
    }


@pytest.fixture
def incorrect_email() -> dict:
    return {"email": "incorrect_email"}


@pytest.fixture
def incorrect_phone() -> dict:
    return {"phone": "incorrect_phone"}


@pytest.fixture
def incorrect_date() -> dict:
    return {"date_of_birth": "01 01 2000"}
