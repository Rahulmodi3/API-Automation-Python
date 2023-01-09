from RestfulBooker.src.utilities.requestsUtility import RequestsUtility
from RestfulBooker.src.utilities.genericUtilities import generate_random_firstname_and_lastname
from datetime import timedelta, date
import logging as logger


class BookingHelper:
    def __init__(self):
        self.req_obj = RequestsUtility()

    def get_booking_by_id(self, bookingid=None):
        r"""Returns a specific booking info based upon the booking id provided
        :param bookingid: pass bookingid for whom you want to get info
        :return: : json Response based on provided booking id """

        # If you not pass bookingid than by default it will set bookingid = 1
        if not bookingid:
            bookingid = 1

        booking_json = self.req_obj.get(endpoint=f"booking/{bookingid}")
        return booking_json

    def create_payload(self, firstname=None, lastname=None, totalprice=None, depositpaid=True, checkindate=None,
                       checkoutdate=None, **kwargs):
        r""" It will return payload for create or update booking"""

        fullname = generate_random_firstname_and_lastname()

        # If firstname is not given than generate random name
        if not firstname:
            firstname = fullname['firstname']

        # If lastname is not given than generate random name
        if not lastname:
            lastname = fullname['lastname']

        # If totalprice is not given than set price = 500
        if not totalprice:
            totalprice = 500

        todaydate = date.today()

        if not checkindate:
            _checkindate = todaydate - timedelta(days=10)
            checkindate = date.isoformat(_checkindate)

        if not checkoutdate:
            _checkoutdate = todaydate - timedelta(days=5)
            checkoutdate = date.isoformat(_checkoutdate)

        # generating payload
        payload = dict()
        payload['firstname'] = firstname
        payload['lastname'] = lastname
        payload['totalprice'] = totalprice
        payload['depositpaid'] = depositpaid
        bookingdates = dict()  # creating dict for checking and checkout date
        bookingdates['checkin'] = checkindate
        bookingdates['checkout'] = checkoutdate
        payload['bookingdates'] = bookingdates
        payload.update(kwargs)  # additional payload

        return payload


    def create_booking(self, firstname=None, lastname=None, totalprice=None, depositpaid=True, checkindate=None,
                       checkoutdate=None, **kwargs):
        r"""Creates a new booking
        :param firstname: give firstname else it will take random name
        :param lastname: give lastname else it will take random name
        :param totalprice: give totalprice else it will take random price
        :param depositpaid: give depositpaid else it will set True
        :param checkindate: give checkindate (year, month, day) else it will set random date
        :param checkoutdate: give checkoutdate ((year, month, day) else it will set random date
        :return: : json Response it will create booking """

        payload = BookingHelper().create_payload(firstname=firstname, lastname=lastname, totalprice=totalprice,
                                                 depositpaid=depositpaid,
                                                 checkindate=checkindate, checkoutdate=checkoutdate)

        payload.update(kwargs)

        booking_json = self.req_obj.post(endpoint='booking', payload=payload, expected_status_code=200)
        return booking_json


    def update_booking(self, bookingid=None, firstname=None, lastname=None, totalprice=None, depositpaid=True,
                       checkindate=None, checkoutdate=None, **kwargs):

        r""" Update existing booking """

        # If you not pass bookingid than by default it will set bookingid = 1
        if not bookingid:
            bookingid = 1

        payload = BookingHelper().create_payload(firstname=firstname, lastname=lastname, totalprice=totalprice,
                                                 depositpaid=depositpaid,
                                                 checkindate=checkindate, checkoutdate=checkoutdate)

        payload.update(kwargs)

        booking_json = self.req_obj.put(endpoint=f'booking/{bookingid}', payload=payload, expected_status_code=200)
        return booking_json

    def partial_update_booking(self, bookingid, firstname=None, lastname=None, totalprice=None, depositpaid=True,
                               checkindate=None, checkoutdate=None, **kwargs):

        r""" Partial update booking """

        payload = BookingHelper().get_booking_by_id(bookingid=bookingid)

        if firstname is not None:
            payload['firstname'] = firstname

        if lastname is not None:
            payload['lastname'] = lastname

        if totalprice is not None:
            payload['totalprice'] = totalprice

        if depositpaid is not True:
            payload['depositpaid'] = depositpaid

        if checkindate is not None:
            payload['checkindate'] = checkindate

        if checkoutdate is not None:
            payload['checkoutdate'] = checkoutdate

        payload.update(kwargs)

        booking_json = self.req_obj.patch(endpoint=f'booking/{bookingid}', payload=payload, expected_status_code=200)
        return booking_json

    def delete_booking(self,bookingid):
        r""" Delete existing booking"""

        booking_json = self.req_obj.delete(endpoint=f'booking/{bookingid}')
        return booking_json
