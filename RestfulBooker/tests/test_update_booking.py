import pytest
from RestfulBooker.src.helpers.booking_helper import BookingHelper

@pytest.mark.tcid07
@pytest.mark.updatebooking
def test_update_booking():
    book_obj = BookingHelper()

    # if you want to update firstname,lastname or any value than provide to update_booking method
    rs_api = book_obj.update_booking(bookingid=18)

    # verify response
    assert rs_api['firstname'] != '', f" Getting empty first name , actual firstname : {rs_api['firstname']} "
    assert rs_api['lastname'] != '', f" Getting empty first name , actual firstname : {rs_api['lastname']} "
