"""
@name: comment_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Feb 03, 2018
"""

from scrape_data.helpers.utilities import Utilities
from scrape_data.services.request_service import RequestService


class CommentService:
    def __init__(self, post_id):
        self.__postId = post_id
        self.__utilities = Utilities()
        self.__commentParams = self.__utilities.get_comment_params()
        self.__baseUrl = self.__utilities.get_base_url(self.__postId)
        self.__requestUrl = RequestService().get_request_url

    def get_comment(self):
        comments = []
        has_next_page = True
        after = ''

        while has_next_page:
            after = '' if after is '' else '&after=' + after
            url_next = self.__baseUrl + after
            response = self.__requestUrl(url_next, self.__commentParams)

            if 'comments' in response:
                data = response['comments']

                if data != '':

                    for comment in data['data']:
                        if int(comment['comment_count']) > 0:
                            id = comment['id']
                            commentData = self.get_comment_level(id)
                            commentLv = dict()
                            commentLv['data'] = commentData
                            comment['comments'] = commentLv

                        comments.append(comment)

                    if 'paging' in data:
                        after = data['paging']['cursors']['after']
                    else:
                        has_next_page = False

                else:
                    has_next_page = False

            else:
                has_next_page = False

        return comments

    def get_comment_level(self, id):
        comments = []
        has_next_page = True
        url = self.__utilities.get_base_url(id)
        after = ''

        while has_next_page:
            after = '' if after is '' else '&after=' + after
            url_next = url + after
            response = self.__requestUrl(url_next, self.__commentParams)

            if 'comments' in response:
                data = response['comments']

                if data != '':
                    for comment in data['data']:
                        comments.append(comment)

                    if 'paging' not in data:
                        after = data['paging']['cursors']['after']
                    else:
                        has_next_page = False

                else:
                    has_next_page = False

            else:
                has_next_page = False

        return comments


