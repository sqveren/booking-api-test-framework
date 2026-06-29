import pytest
from client.api_client import APIClient
from api.booking_api import BookingAPI
from models.booking_models import Booking, BookingDates

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

@pytest.fixture
def created_booking(booking_api, booking_data, auth_headers):
    response = booking_api.create_booking(booking_data)
    booking_id = response.json()["bookingid"]
    yield booking_id
    booking_api.delete_booking(booking_id, headers=auth_headers)