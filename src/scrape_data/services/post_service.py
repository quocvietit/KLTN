"""
@name: post_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Feb 03, 2018
"""
from scrape_data.helpers.utilities import Utilities
from scrape_data.services.request_service import RequestService
from scrape_data.services.comment_service import CommentService
from scrape_data.services.file_service import FileService


class PagePostService:
    def __init__(self, page_name, file_path):
        self.__pageName = page_name
        self.__utilities = Utilities()
        self.__postParams = self.__utilities.get_post_params()
        self.__baseUrl = self.__utilities.get_base_url(self.__pageName)
        self.__requestUrl = RequestService().get_request_url
        self.__commentService = CommentService
        self.__filePath = file_path
        self.__fileService = FileService

    def get_posts(self):
        f = self.__fileService(self.__filePath + self.__pageName + '_posts')
        has_next_page = True
        after = ''

        while has_next_page:
            after = '' if after is '' else '&after=' + after
            url_next = self.__baseUrl + after
            response = self.__requestUrl(url_next, self.__postParams)

            if 'posts' in response:
                data = response['posts']

                if response != '':

                    for post in data['data']:
                        id = post['id']
                        print "Get post id: ", id

                        comment = self.__commentService(id).get_comment()
                        comments = dict()
                        comments['data'] = comment
                        post['comments'] = comments

                        f.write(post)
                        print "Done"

                    if 'paging' in data:

                        if data['paging']['cursors']['after'] != after[7:]:
                            after = data['paging']['cursors']['after']
                        else:
                            has_next_page = False

                    else:
                        has_next_page = False

                else:
                    has_next_page = False

            else:
                has_next_page = False

