import pytest
import logging as logger
from RestfulBooker.src.helpers.booking_helper import BookingHelper
from RestfulBooker.src.utilities.requestsUtility import RequestsUtility


@pytest.mark.tcid04
@pytest.mark.getbookingbyfilter
def test_get_booking_by_filter():
    # parameters
    params = dict()
    params['firstname'] = 'John'
    params['lastname'] = 'Smith'
    req_obj = RequestsUtility()

    # get booking id by firstname=Josh
    rs_api = req_obj.get(endpoint='booking', params=params)
    logger.info(f"Total same firstname booking id : {len(rs_api)}")
    get_booking_id = rs_api[len(rs_api)-1]['bookingid']
    assert get_booking_id != '', f"Getting empty booking and actual : {get_booking_id}"

    # assert with booking info
    booking_josn = BookingHelper().get_booking_by_id(bookingid=get_booking_id)
    # verify response
    assert booking_josn['firstname'] == 'John', f" Getting empty first name , actual firstname : {booking_josn['firstname']} "
    assert booking_josn['lastname'] == 'Smith', f" Getting empty first name , actual firstname : {booking_josn['lastname']} "
