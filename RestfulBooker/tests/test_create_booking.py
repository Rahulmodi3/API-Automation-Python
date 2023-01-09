import pytest
import logging as logger
from RestfulBooker.src.helpers.booking_helper import BookingHelper


@pytest.mark.tcid06
@pytest.mark.createbooking
def test_create_booking():
    book_obj = BookingHelper()

    rs_api = book_obj.create_booking()
    assert rs_api['bookingid'] != '', f"Getting empty booking and actaul booking id : {rs_api['bookingid']}"
    logger.info(f"get booking id {rs_api['bookingid']}")
