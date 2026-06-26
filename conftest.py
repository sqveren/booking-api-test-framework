import pytest
from client.api_client import APIClient
from api.booking_api import BookingAPI

@pytest.fixture(scope="session")
def booking_api():
    client = APIClient("https://restful-booker.herokuapp.com")
    return BookingAPI(client)

@pytest.fixture
def booking_data():
    return {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }