"""
@name: scrape_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Feb 03, 2018
"""
from scrape_data.services.page_service import PageDetailService
from scrape_data.services.post_service import PagePostService
from scrape_data.services.file_service import FileService


class ScrapeService:
    def __init__(self, page_name, file_path):
        self.__pageName = page_name
        self.__filePath = file_path
        self.__pageService = PageDetailService(self.__pageName, self.__filePath)
        self.__postService = PagePostService(self.__pageName, self.__filePath)
        self.__fileService = FileService

    def start(self):
        self.scrape_page_info()
        self.scrape_post_info()

    def scrape_page_info(self):
        self.__pageService.get_page_info()


    def scrape_post_info(self):
        self.__postService.get_posts()





