import pytest
from client.api_client import APIClient
from api.booking_api import BookingAPI
from models.booking_model import Booking, BookingDates

@pytest.fixture(scope="session")
def booking_api():
    client = APIClient("https://restful-booker.herokuapp.com")
    return BookingAPI(client)

@pytest.fixture(scope="session")
def auth_headers(booking_api):
    token = booking_api.auth().json()["token"]
    return {"Cookie": f"token={token}"}

@pytest.fixture
def booking_data():
    return Booking(
        firstname="Jim",
        lastname="Brown",
        totalprice=111,
        depositpaid=True,
        bookingdates=BookingDates(
            checkin="2024-01-01",
            checkout="2024-01-05"
        ),
        additionalneeds="Breakfast"
    ).to_dict()