import pytest
import allure
from utils.assertions import assert_status_code


@allure.feature("Booking")
@allure.story("Delete booking")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_delete_booking(booking_api, created_booking, auth_headers):
    response = booking_api.delete_booking(created_booking, headers=auth_headers)
    assert_status_code(response, 201)


@allure.feature("Booking")
@allure.story("Delete booking - negative")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_delete_booking_without_auth(booking_api, created_booking):
    response = booking_api.delete_booking(created_booking)
    assert_status_code(response, 403)


@allure.feature("Booking")
@allure.story("Delete booking - negative")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_delete_nonexistent_booking(booking_api, auth_headers):
    response = booking_api.delete_booking(999999999, headers=auth_headers)
    assert response.status_code in [404, 405]