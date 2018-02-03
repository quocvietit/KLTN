"""
@name: request_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Jan 31, 2018
"""

import time
import requests


class RequestService:
    def __init__(self):
        self.__limit_request = 10

    def set_limit_request(self, limit_request):
        self.__limit_request = limit_request

    # return response url type json
    def get_request_url(self, url, params):
        count = 0
        while count < self.__limit_request:
            try:
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    return response.json()
            except Exception as e:
                print e
                time.sleep(5)

            count = count + 1


