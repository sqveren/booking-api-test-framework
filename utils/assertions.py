def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, (
        f"Expected {expected_code}, got {response.status_code}. "
        f"Response: {response.text}"
    )

def assert_booking_fields(response_json, expected_data):
    assert response_json["firstname"] == expected_data["firstname"]
    assert response_json["lastname"] == expected_data["lastname"]
    assert response_json["totalprice"] == expected_data["totalprice"]