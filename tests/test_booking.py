


def test_create_booking(booking_api, booking_data):
    response = booking_api.create_booking(booking_data)

    assert response.status_code == 200
    assert response.json()["bookingid"] is not None



def test_update_booking(booking_api, booking_data):
    created = booking_api.create_booking(booking_data)
    booking_id = created.json()["bookingid"]

    updated_data = {**booking_data, "firstname": "Yurii", "totalprice": 999}
    response = booking_api.update_booking(booking_id,updated_data)

    assert response.status_code == 200
    assert response.json()["firstname"] == "Yurii"
    assert response.json()["totalprice"] == 999