"""
@name: utilities.py
@author: Vuong Quoc Viet
@version: 1.0
@since: Jan 30, 2018
"""

from scrape_data.core.token import Token


class Utilities:
    def __init__(self):
        self.__baseUrl = "https://graph.facebook.com/v2.11/"
        self.__token = Token().get_token()

        self.__header = {
            "Accept": "application/json",
            "Content-type": "application/json"
        }

        self.__pageDetail = {
            'fields': 'id,'
                      + 'name,'
                      + 'about,'
                      + 'fan_count,'
                      + 'category,'
                      + 'location,'
                      + 'username,'
                      + 'link'
        }

        self.__reactionParams = 'reactions.limit(0).summary(total_count),' \
                                + 'reactions.type(LIKE).limit(0).summary(total_count).as(like),' \
                                + 'reactions.type(LOVE).limit(0).summary(total_count).as(love),' \
                                + 'reactions.type(HAHA).limit(0).summary(total_count).as(haha),' \
                                + 'reactions.type(WOW).limit(0).summary(total_count).as(wow),' \
                                + 'reactions.type(SAD).limit(0).summary(total_count).as(sad),' \
                                + 'reactions.type(ANGRY).limit(0).summary(total_count).as(angry)'

        self.__postParams = {
            'fields': 'id,'
                      + 'created_time,'
                      + 'link,'
                      + 'message,'
                      + 'type,'
                      + 'from,'
                      + 'status_type,'
                      + 'shares,'
                      + 'comments.limit(0).summary(true),'
                      + self.__reactionParams
        }

        self.__commentParams = {
            'fields': 'id,'
                      + 'created_time,'
                      + 'link,'
                      + 'message,'
                      + 'comment_count,'
                      + self.__reactionParams
        }

    def get_base_url(self, id):
        return self.__baseUrl + id + '?access_token=' + '335667203583506|NonMVS1dqIaQk5PsX1nvJnU17Yo' + '&limit=100'

    def get_post_params(self):
        return self.__postParams

    def get_header(self):
        return self.__header

    def get_page_detail(self):
        return self.__pageDetail

    def get_reaction_params(self):
        return self.__reactionParams

    def get_comment_params(self):
        return self.__commentParams
