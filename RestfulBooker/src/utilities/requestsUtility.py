import requests
from requests.auth import HTTPBasicAuth
from RestfulBooker.src.configs.host_config import API_HOSTS, API_BASIC_AUTH
import logging as logger
import json


class RequestsUtility:

    def __init__(self):

        self.base_url = API_HOSTS['base_url']
        self.auth = HTTPBasicAuth(username=API_BASIC_AUTH['username'], password=API_BASIC_AUTH['password'])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status code." \
                                                              f"Actual status code {self.status_code} and expected is {self.expected_status_code}," \
                                                              f"URL: {self.url}, Response Json: {self.rs_json}"

    def get(self, endpoint, payload=None, params=None, headers=None, expected_status_code=200):
        r"""Sends a GET request.

        :param params:
        :param endpoint: pass endpoint
        :param payload: (optional) Dictionary, pass body
        :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string
        :param headers: (optional) Dictionary, pass header
        :param expected_status_code: (optional) pass status code if your get request give other than 200 response code .
        :return: : json Response
        """

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), params=params, headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code

        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()

        'Calling assert status code method'
        self.assert_status_code()  # verify status code

        logger.info(f"GET API response: {self.rs_json}")

        return self.rs_json

    def post(self, endpoint, payload=None, headers=None, expected_status_code=201):
        r"""Sends a POST request.

        :param endpoint: pass endpoint
        :param payload: (optional) Dictionary, pass body
        :param headers: (optional) Dictionary , pass header
        :param expected_status_code: (optional) pass status code if your post request give other than 201 response code .
        :return: : json Response
        """
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        rs_api = requests.post(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()

        'Calling assert status code method'
        self.assert_status_code()  # verify status code

        logger.info(f"POST API response: {self.rs_json}")

        return self.rs_json

    def put(self, endpoint, payload=None, headers=None, expected_status_code=200):
        r"""Sends a PUT request.

        :param endpoint: pass endpoint
        :param payload: (optional) Dictionary, pass body
        :param headers: (optional) Dictionary , pass header
        :param expected_status_code: (optional) pass status code if your put request give other than 200 response code .
        :return: : json Response
        """
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        rs_api = requests.put(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()

        'Calling assert status code method'
        self.assert_status_code()  # verify status code

        logger.info(f"PUT API response: {self.rs_json}")

        return self.rs_json

    def patch(self, endpoint, payload=None, headers=None, expected_status_code=200):
        r"""Sends a PATCH request.

        :param endpoint: pass endpoint
        :param payload: (optional) Dictionary, pass body
        :param headers: (optional) Dictionary , pass header
        :param expected_status_code: (optional) pass status code if your put request give other than 200 response code .
        :return: : json Response
        """
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        rs_api = requests.patch(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()

        'Calling assert status code method'
        self.assert_status_code()  # verify status code

        logger.info(f"PATCH API response: {self.rs_json}")

        return self.rs_json

    def delete(self, endpoint, payload=None, headers=None, expected_status_code=201):
        r"""Sends a DELETE request.

        :param endpoint: pass endpoint
        :param payload: (optional) Dictionary, pass body
        :param headers: (optional) Dictionary , pass header
        :param expected_status_code: (optional) pass status code if your put request give other than 201 response code .
        :return: : Response
        """

        self.url = self.base_url + endpoint

        rs_api = requests.delete(url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code

        'Calling assert status code method'
        self.assert_status_code()  # verify status code

        logger.info(f"DELETE API response: {rs_api}")

        return rs_api
