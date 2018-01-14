import os


class Token:
    def __init__(self):
        self.__AppID = os.environ.get('APP_ID')
        self.__AppSecret = os.environ.get('APP_SECRET')

    # Get My App ID
    def get_app_id(self):
        return str(self.__AppID)

    # Get My App secret
    def get_app_secret(self):
        return str(self.__AppSecret)

    # Get Token
    # return  [AppID]|[AppSecrect]
    def get_token(self):
        return "{}|{}".format(self.get_app_id(), self.get_app_secret())
