"""
@name: utilities.py
@author: Vuong Quoc Viet
@version: 1.0
@since: Jan 30, 2018
"""

from scrape_data.core.token import Token


class Utilities:
    def __init__(self):
        self.__BASE_URL = "https://graph.facebook.com/v2.11"
        self.__PARAMETERS = "&limit={}&access_token={}"
        self.__AFTER = "&after={}"
        self.__ACCESS_TOKEN = Token().get_token()

    def get_base_url(self):
        return self.__BASE_URL

    def get_parameters(self, limit_item=100):
        return self.__PARAMETERS.format(limit_item, self.__ACCESS_TOKEN)

    def get_after(self, after_url):
        return self.__AFTER.format(after_url)
