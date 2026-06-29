import pytest
import allure
from utils.assertions import assert_status_code, assert_booking_fields


@allure.feature("Booking")
@allure.story("Get all bookings")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_get_all_bookings(booking_api):
    response = booking_api.get_all_bookings()
    assert_status_code(response, 200)
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


@allure.feature("Booking")
@allure.story("Get booking by ID")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_get_booking_by_id(booking_api, created_booking, booking_data):
    response = booking_api.get_booking(created_booking)
    assert_status_code(response, 200)
    assert_booking_fields(response.json(), booking_data)


@allure.feature("Booking")
@allure.story("Get booking - negative")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_nonexistent_booking(booking_api):
    response = booking_api.get_booking(999999999)
    assert_status_code(response, 404)


@allure.feature("Booking")
@allure.story("Get booking - negative")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_get_booking_negative_id(booking_api):
    response = booking_api.get_booking(-1)
    assert_status_code(response, 404)