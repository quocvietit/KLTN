"""
@name: page_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Feb 03, 2018
"""
from scrape_data.helpers.utilities import Utilities
from scrape_data.services.request_service import RequestService
from scrape_data.services.file_service import FileService

class PageDetailService:
    def __init__(self, page_name, file_path):
        self.__pageName = page_name
        self.__utilities = Utilities()
        self.__pageParams = self.__utilities.get_page_detail()
        self.__baseUrl = self.__utilities.get_base_url(self.__pageName)
        self.__filePath = file_path
        self.__fileService = FileService

    def get_page_info(self):
        f = self.__fileService(self.__filePath + self.__pageName + '_info')
        try:
            req = RequestService()
            response = req.get_request_url(self.__baseUrl, self.__pageParams)
            f.write(response)
            print "Done get page information !"
        except Exception as ex:
            print ex
