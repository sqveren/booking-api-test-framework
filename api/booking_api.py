from client.api_client import APIClient

class BookingAPI:
    def __init__(self, client):
        self.client = client

    def auth(self):
        data = {"username": "admin", "password": "password123"}
        return self.client.post("/auth", data)

    def create_booking(self, data):
        return self.client.post("/booking", data)

    def get_booking(self, booking_id):
        return self.client.get(f"/booking/{booking_id}")

    def update_booking(self, booking_id, data, headers=None):
        return self.client.put(f"/booking/{booking_id}", data, headers=headers)

    def delete_booking(self, booking_id, headers=None):
        return self.client.delete(f"/booking/{booking_id}", headers=headers)

    def partial_update_booking(self,booking_id, data):
        return self.client.patch(f"/booking/{booking_id}", data)

    def get_all_bookings(self):
        return self.client.get("/booking")

