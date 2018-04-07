"""
@name: get_data_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Feb 28, 2018
"""
import json


class GetDataService:
    def __init__(self, json_data):
        self.__data = json.loads(json_data)
        self.__id = 'id'
        self.__link = 'link'
        self.__createdTime = 'created_time'
        self.__type = 'type'
        self.__statusType = 'status_type'
        self.__message = 'message'
        self.__comments = 'comments'
        self.__shares = 'shares'
        self.__reactions = 'reactions'
        self.__like = 'like'
        self.__wow = 'wow'
        self.__haha = 'haha'
        self.__sad = 'sad'
        self.__love = 'love'
        self.__angry = 'angry'
        self.__summary = 'summary'
        self.__totalCount = 'total_count'
        self.__from = 'from'
        self.__name = 'name'
        self.__count = 'count'

    def get_post_id(self):
        return self.__data[self.__id]

    def get_link_post(self):
        if self.__link in self.__data:
            return self.__data[self.__link]
        return 'No link'

    def get_created_time(self):
        if self.__createdTime in self.__data:
            return self.__data[self.__createdTime]
        return ''

    def get_post_type(self):
        if self.__type in self.__data:
            return self.__data[self.__type]
        return 'No type'

    def get_status_type(self):
        if self.__statusType in self.__data:
            return self.__data[self.__statusType]
        return 'published_story'

    def get_message(self):
        if self.__message in self.__data:
            return self.__data[self.__message]
        return 'No message'

    def get_number_comment(self):
        if self.__comments in self.__data:
            return self.__data[self.__comments][self.__summary][self.__totalCount]
        return 0

    def get_number_share(self):
        if self.__shares in self.__data:
            return self.__data[self.__shares][self.__count]
        return 0

    def get_number_reaction(self):
        if self.__reactions in self.__data:
            return self.__data[self.__reactions][self.__summary][self.__totalCount]
        return 0

    def get_number_like(self):
        if self.__like in self.__data:
            return self.__data[self.__like][self.__summary][self.__totalCount]
        return 0

    def get_number_wow(self):
        if self.__wow in self.__data:
            return self.__data[self.__wow][self.__summary][self.__totalCount]
        return 0

    def get_number_haha(self):
        if self.__haha in self.__data:
            return self.__data[self.__haha][self.__summary][self.__totalCount]
        return 0

    def get_number_sad(self):
        if self.__sad in self.__data:
            return self.__data[self.__sad][self.__summary][self.__totalCount]
        return 0

    def get_number_love(self):
        if self.__love in self.__data:
            return self.__data[self.__love][self.__summary][self.__totalCount]
        return 0

    def get_number_angry(self):
        if self.__angry in self.__data:
            return self.__data[self.__angry][self.__summary][self.__totalCount]
        return 0

    def get_from(self):
        if self.__from in self.__data:
            return self.__data[self.__from][self.__name]
        return ''
