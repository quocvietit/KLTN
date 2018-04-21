"""
@name: remove_punctuation_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import logging
from string import punctuation


class RemovePunctuationService:
    def __init__(self):
        self.__punctuation = punctuation

    # create dictionnary
    def create_dictionary_punctuation(self):
        logging.debug("Create dictionary punctuation")
        dictionary = {}
        for i in set(self.__punctuation):
            dictionary[i] = " "
        return dictionary

    # remove punctuation
    def replace_all(self, text, dictionary):
        logging.debug("Replace punctuation")
        for i, j in dictionary.iteritems():
            text = text.replace(i, j)
        return text

    def remove_punctuation(self, text):
        logging.debug("Remove punctuation")
        dictionary = self.create_dictionary_punctuation()
        return self.replace_all(text, dictionary)
