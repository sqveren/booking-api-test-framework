import pytest
from utils.assertions import assert_status_code, assert_booking_fields


@pytest.mark.smoke
def test_get_all_bookings(booking_api):
    response = booking_api.get_all_bookings()
    assert_status_code(response, 200)
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


@pytest.mark.smoke
def test_get_booking_by_id(booking_api, created_booking, booking_data):
    response = booking_api.get_booking(created_booking)
    assert_status_code(response, 200)
    assert_booking_fields(response.json(), booking_data)


@pytest.mark.regression
def test_get_nonexistent_booking(booking_api):
    response = booking_api.get_booking(999999999)
    assert_status_code(response, 404)


@pytest.mark.regression
def test_get_booking_negative_id(booking_api):
    response = booking_api.get_booking(-1)
    assert_status_code(response, 404)