from dataclasses import dataclass

@dataclass
class BookingDates:
    checkin: str
    checkout: str

@dataclass
class Booking:
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str = ""

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": {
                "checkin": self.bookingdates.checkin,
                "checkout": self.bookingdates.checkout
            },
            "additionalneeds": self.additionalneeds
        }