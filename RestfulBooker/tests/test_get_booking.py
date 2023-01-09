import pytest
import logging as logger
from RestfulBooker.src.utilities.requestsUtility import RequestsUtility
from RestfulBooker.src.helpers.booking_helper import BookingHelper


class TestGetBooking:

    @pytest.mark.tcid02
    @pytest.mark.getallbooking
    def test_get_all_booking_ids(self):
        # send request
        rs_api = RequestsUtility().get(endpoint='booking')

        # verify response
        get_booking_id = rs_api[0]['bookingid']
        logger.info(f"1st booking id : {get_booking_id}")
        logger.info(f"Total available booking is : {len(rs_api)}")
        assert get_booking_id != '', f"Getting empty booking and actual token is {get_booking_id}"

    @pytest.mark.tcid03
    @pytest.mark.getspecificbooking
    def test_get_specific_booking(self):
        # send request
        rs_api = BookingHelper().get_booking_by_id(bookingid=8)

        # verify response
        assert rs_api['firstname'] != '', f" Getting empty first name , actual firstname : {rs_api['firstname']} "
        assert rs_api['lastname'] != '', f" Getting empty first name , actual firstname : {rs_api['lastname']} "
