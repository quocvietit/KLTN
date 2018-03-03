"""
@name: mapper_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Mar 03, 2018
"""
import datetime
import dateutil.parser
from cleaning_data.service.get_data_service import GetDataService
from cleaning_data.models.information_post import InformationPost


class MapperService:
    def __init__(self, ):
        self.__data = ''
        self.__dataService = ''
        #self.__formatDate = '%Y-%m-%dT%H:%M:%S.%fZ'

    def set_data(self, json_data):
        self.__data = json_data

    def mapper(self, json_data):
        self.set_data(json_data)

        informationPost = InformationPost()
        self.__dataService = GetDataService(self.__data)

        try:
            informationPost.id = self.__dataService.get_post_id()
            informationPost.link = self.__dataService.get_link_post()
            informationPost.from_name = self.__dataService.get_from()
            informationPost.type = self.__dataService.get_post_type()
            informationPost.statusType = self.__dataService.get_status_type()
            informationPost.message = self.__dataService.get_message()
            informationPost.comments = self.__dataService.get_number_comment()
            informationPost.shares = self.__dataService.get_number_share()
            informationPost.reactions = self.__dataService.get_number_reaction()
            informationPost.like = self.__dataService.get_number_like()
            informationPost.love = self.__dataService.get_number_love()
            informationPost.haha = self.__dataService.get_number_haha()
            informationPost.wow = self.__dataService.get_number_wow()
            informationPost.sad = self.__dataService.get_number_sad()
            informationPost.angry = self.__dataService.get_number_angry()

            # Format date
            date = self.format_date(self.__dataService.get_created_time())
            informationPost.created_time_year = date.year
            informationPost.created_time_month = date.month
            informationPost.created_time_day = date.day
            informationPost.created_time_hour = date.hour
            informationPost.created_time_minute = date.minute
            informationPost.created_time_second = date.second

            return informationPost.__dict__

        except Exception as ex:
            print "Error mapper: ", ex

    def format_date(self, date):
        try:
            #date = datetime.datetime.strptime(date, self.__formatDate)
            date = dateutil.parser.parse('2014-05-18T12:19:24+04:00')
            return date
        except Exception as ex:
            print "Error date: ", ex

        return None
