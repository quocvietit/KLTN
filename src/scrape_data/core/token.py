"""
@name: token.py
@author: Vuong Quoc Viet
@version: 1.0
@since: Jan 30, 2018
"""

import os


class Token:
    def __init__(self):
        self.__APP_ID = os.environ.get('APP_ID')
        self.__APP_SECRET = os.environ.get('APP_SECRET')
        self.__TOKEN = "{}|{}".format(self.__APP_ID, self.__APP_SECRET)

    def get_app_id(self):
        return self.__APP_ID

    def get_app_secret(self):
        return self.__APP_SECRET

    def get_token(self):
        return self.__TOKEN
