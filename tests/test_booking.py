import pytest
import allure
from utils.assertions import assert_status_code, assert_booking_fields


@allure.feature("Booking")
@allure.story("Create booking")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_create_booking(booking_api, booking_data):
    response = booking_api.create_booking(booking_data)
    assert_status_code(response, 200)
    assert response.json()["bookingid"] is not None


@allure.feature("Booking")
@allure.story("Update booking")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_update_booking(booking_api, booking_data, auth_headers):
    created = booking_api.create_booking(booking_data)
    booking_id = created.json()["bookingid"]
    updated_data = {**booking_data, "firstname": "Yurii", "totalprice": 999}
    response = booking_api.update_booking(booking_id, updated_data, headers=auth_headers)
    assert_status_code(response, 200)
    assert_booking_fields(response.json(), updated_data)


@allure.feature("Booking")
@allure.story("Create booking - negative")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_create_booking_invalid_data(booking_api):
    response = booking_api.create_booking({})
    assert response.status_code in [400, 500]


@allure.feature("Booking")
@allure.story("Create booking - negative")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_create_booking_missing_required_fields(booking_api):
    response = booking_api.create_booking({"firstname": "Jim"})
    assert response.status_code in [400, 500]


@allure.feature("Booking")
@allure.story("Update booking - negative")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_update_booking_without_auth(booking_api, booking_data):
    created = booking_api.create_booking(booking_data)
    booking_id = created.json()["bookingid"]
    response = booking_api.update_booking(booking_id, booking_data)
    assert response.status_code == 403


@allure.feature("Booking")
@allure.story("Update booking - negative")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
def test_update_booking_invalid_token(booking_api, booking_data):
    created = booking_api.create_booking(booking_data)
    booking_id = created.json()["bookingid"]
    headers = {"Cookie": "token=invalidtoken123"}
    response = booking_api.update_booking(booking_id, booking_data, headers=headers)
    assert response.status_code == 403