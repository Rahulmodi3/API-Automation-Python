import pytest
import logging as logger
from RestfulBooker.src.helpers.booking_helper import BookingHelper



@pytest.mark.tcid09
@pytest.mark.deletebooking
def test_delete_booking():
    book_obj = BookingHelper()
    rs_api = book_obj.delete_booking(bookingid=8240)

    assert rs_api.text == 'Created', f"Actual Result : {rs_api.text} and Expected Result : Created"

    logger.info(f"response {rs_api.text}")
