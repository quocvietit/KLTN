"""
@name: encode
@author: Vuong Quoc Viet
@version: 1.0
@since: Feb 04, 2018
"""


class Encode:
    def __init__(self):
        self.__text = ''

    def unicode_encode(self, text):
        self.__text = text
        return self.__text.encode("utf-8")
