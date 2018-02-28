"""
@name: data_post
@author: Vuong Quoc Viet
@version: 1.0
@since: Feb 28, 2018
"""


class DataPost:
    def __init__(self, json_data):
        self.__data = json_data

    def get_post_id(self):
        return self.__data['id']

    def get_link_post(self):
        return self.__data['link']

    def get_created_time(self):
        return self.__data['created_time']

    def get_post_type(self):
        return self.__data['type']

    def get_status_type(self):
        status_type = 'status_type'
        if status_type in self.__data:
            return self.__data[status_type]
        return ''

    def get_message(self):
        if 'message' in self.__data:
            return self.__data['message']
        return ''

    def get_number_comment(self):
        return self.__data['comments']['summary']['total_count']

    def get_number_shares(self):
        return self.__data['shares']['count']

    def get_number_reactions(self):
        return self.__data['reactions']['summary']['total_count']

    def get_number_like(self):
        return self.__data['like']['summary']['total_count']

    def get_number_wow(self):
        return self.__data['wow']['summary']['total_count']

    def get_number_haha(self):
        return self.__data['haha']['summary']['total_count']

    def get_number_sad(self):
        return self.__data['sad']['summary']['total_count']

    def get_number_love(self):
        return self.__data['love']['summary']['total_count']

    def get_number_sad(self):
        return self.__data['sad']['summary']['total_count']

    def get_from(self):
        return self.__data['from']['name']
