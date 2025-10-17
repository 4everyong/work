import pytest
import requests
from faker import Faker
from constants import BASE_URL, HEADERS

faker = Faker()

@pytest.fixture(scope="session")
def auth_session():
    json = {
        "username": "admin",
        "password": "password123"
    }
    session = requests.Session()
    session.headers.update(HEADERS)

    response = requests.post(
        f"{BASE_URL}/auth",
        headers=HEADERS,
        json=json
    )
    assert response.status_code == 200, "Ошибка авторизации"
    token = response.json().get("token")
    assert token is not None, "В ответе не оказалось токена"
    session.headers.update({"Cookie": f"token={token}"})
    return session
@pytest.fixture()
def booking_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Piano"
    }
@pytest.fixture()
def booking_data_update():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-04-05",
            "checkout": "2025-04-08"
        },
        "additionalneeds": "Piano"
    }