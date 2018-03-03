"""
@name: covert_json_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Mar 03, 2018
"""
import json


class ConvertJsonService:
    def __init__(self):
        self.__data = ''

    def get_json(self, object_data):
        try:
            self.__data = object_data
            json_data = json.dumps(self.__data)
            return json_data
        except Exception as ex:
            print ex
