import pytest
from RestfulBooker.src.helpers.booking_helper import BookingHelper

@pytest.mark.tcid08
@pytest.mark.partialbooking
def test_partial_booking():
    book_obj = BookingHelper()

    rs_api = book_obj.partial_update_booking(bookingid=18, firstname='test_update', totalprice=1000)

    # verify response
    assert rs_api['firstname'] == 'test_update', f" first name is not match , actual firstname : {rs_api['firstname']}"
    assert rs_api['lastname'] != '', f" Getting empty first name , actual firstname : {rs_api['lastname']}"

