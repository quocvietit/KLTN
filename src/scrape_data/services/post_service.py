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
    def __init__(self, page_name, file_path, since, until):
        self.__pageName = page_name
        self.__utilities = Utilities()
        self.__since = '&since={}'.format(since)
        self.__until = '&until={}'.format(until)
        self.__timeFile = since[:4] if since[:4] == until[:4] else since[:4] + '_' + until[:4]
        self.__postParams = self.__utilities.get_post_params()
        self.__baseUrl = self.__utilities.get_base_url(self.__pageName + '/posts')
        self.__requestUrl = RequestService().get_request_url
        self.__commentService = CommentService
        self.__filePath = file_path
        self.__fileService = FileService

    def get_posts(self):
        f = self.__fileService(self.__filePath + self.__pageName + '_posts_' + self.__timeFile)
        has_next_page = True
        url_next = self.__baseUrl + self.__since + self.__until
        count = 0
        while has_next_page:
            data = self.__requestUrl(url_next, self.__postParams)
            print url_next

            if data is not None and 'data' in data:

                for post in data['data']:
                    count += 1
                    id = post['id']

                    try:
                        comment = self.__commentService(id).get_comment()
                        post['comments']['data'] = comment

                    except Exception as ex:
                        print ex

                    f.write(post)

                if 'paging' in data:
                    paging = data['paging']

                    if 'next' in paging:
                        url_next = paging['next']
                    else:
                        has_next_page = False

                else:
                    has_next_page = False

            else:
                has_next_page = False

        print "Total_count: ", count
