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
        self.__requestUrl = RequestService().get_request_url

    def get_comment(self):
        comments = []
        has_next_page = True
        url_next = self.__utilities.get_base_url(self.__postId + '/comments')

        while has_next_page:
            try:
                data = self.__requestUrl(url_next, self.__commentParams)

                if data is not None and 'data' in data:
                    for comment in data['data']:
                        if 'comment_count' in comment and int(comment['comment_count']) > 0:
                            id = comment['id']
                            
                            commentData = self.get_comment_level(id)
                            commentLv = dict()
                            commentLv['data'] = commentData
                            commentLv['total_count'] = len(commentData)
                            comment['comments'] = commentLv

                        comments.append(comment)

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

            except Exception as ex:
                print ex
                has_next_page = False

        return comments

    def get_comment_level(self, id):
        comments = []
        has_next_page = True
        url_next = self.__utilities.get_base_url(id + "/comments")

        while has_next_page:
            try:
                data = self.__requestUrl(url_next, self.__commentParams)

                if data is not None and'data' in data:
                    for comment in data['data']:
                        comments.append(comment)

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

            except Exception as ex:
                print ex
                has_next_page = False

        return comments
