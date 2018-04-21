"""
@name: stop_word_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import logging
from nltk.corpus import stopwords




class StopWordService:
    def __init__(self, path, language):
        self.__language = language
        self.__file = "{}/{}_{}.txt".format(path, "stopwords", language)
        self.__stopWords = set(stopwords.words(language))

    # get stop words
    def get_stop_words(self):
        logging.debug("Get stop words")
        try:
            with(open(self.__file, "r")) as f:
                stop_words = set(f.readlines())
                f.close()
                if len(stop_words) < len(self.__stopWords):
                    self.__stopWords = stop_words
        except IOError as err:
            print ("Error: " + str(err))
            logging.error(str(err))

        return self.__stopWords

    # set stop words
    def set_stop_words(self, stop_word):
        logging.debug("Set stop words")
        try:
            self.__stopWords = self.get_stop_words()
            print stop_word in self.__stopWords
            if stop_word not in self.__stopWords:
                with(open(self.__file, "ab+", )) as f:
                    f.write("\n")
                    f.write(stop_word)
        except IOError as err:
            print ("Error: " + str(err))
            logging.error(str(err))

    def remove_stop_words(self, text):
        logging.debug("Remove stop words")
        self.__stopWords = self.get_stop_words()
        text_clean = " ".join([word for word in text.lower().split() if word not in self.__stopWords])
        return text_clean