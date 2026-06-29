


def test_create_booking(booking_api, booking_data):
    response = booking_api.create_booking(booking_data)

    assert response.status_code == 200
    assert response.json()["bookingid"] is not None



def test_update_booking(booking_api, booking_data):
    created = booking_api.create_booking(booking_data)
    booking_id = created.json()["bookingid"]

    token = booking_api.auth().json()["token"]
    headers = {"Cookie": f"token={token}"}

    updated_data = {**booking_data, "firstname": "Yurii", "totalprice": 999}
    response = booking_api.update_booking(booking_id,updated_data, headers=headers)

    assert response.status_code == 200
    assert response.json()["firstname"] == "Yurii"
    assert response.json()["totalprice"] == 999


def test_get_nonexisting_booking(booking_api):
        response = booking_api.get_booking(99999999)
        assert response.status_code == 404

def test_get_negative_booking(booking_api):
        response = booking_api.get_booking(-1)
        assert response.status_code == 404

def test_create_booking_invalid_data(booking_api):
        response = booking_api.create_booking({})
        assert response.status_code in [400,500]

def test_create_booking_missing_required_fields(booking_api):
        response = booking_api.create_booking({"firstname": "Jim"})
        assert response.status_code in [400,500]

def test_update_booking_without_auth(booking_api, booking_data):
        created = booking_api.create_booking(booking_data)
        booking_id = created.json()["bookingid"]
        response = booking_api.update_booking(booking_id, booking_data)
        assert response.status_code == 403

def test_update_booking_invalid_token(booking_api, booking_data):
        created = booking_api.create_booking(booking_data)
        booking_id = created.json()["bookingid"]
        headers = {"Cookie": "token=invalidtoken123"}
        response = booking_api.update_booking(booking_id, booking_data, headers=headers)
        assert response.status_code == 403

