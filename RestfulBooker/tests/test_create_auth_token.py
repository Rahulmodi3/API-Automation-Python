import pytest
import logging as logger

from RestfulBooker.src.configs.host_config import API_BASIC_AUTH
from RestfulBooker.src.utilities.requestsUtility import RequestsUtility


@pytest.mark.tcid01
@pytest.mark.auth
def test_create_token():

    # send request
    rs_api = RequestsUtility().post(endpoint='auth', payload=API_BASIC_AUTH, expected_status_code=200)

    # get token
    get_token = rs_api['token']
    assert get_token is not None, f"Getting empty token and actual token is {get_token}"


