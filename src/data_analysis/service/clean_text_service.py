"""
@name: clean_text_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import logging

from data_analysis.service.stop_word_service import StopWordService
from data_analysis.service.lemmatization_service import LemmatizationService
from data_analysis.service.remove_digit_service import RemoveDigitService
from data_analysis.service.remove_punctuation_service import RemovePunctuationService
from data_analysis import setting

class CleanTextService:
    def __init__(self):
        self.__cleanStopWords = StopWordService(setting.DATA, setting.LANGUAGE).remove_stop_words
        self.__leamatization = LemmatizationService().start
        self.__cleanDigits = RemoveDigitService().start
        self.__cleanPunctuation = RemovePunctuationService().remove_punctuation

    def start(self, text):
        logging.info("Clean text")
        text_ascii = self.remove_ascii(text)
        text_not_punctuation = self.__cleanPunctuation(text_ascii)
        text_not_stop_words = self.__cleanStopWords(text_not_punctuation)
        text_not_digit = self.__cleanDigits(text_not_stop_words)
        text_lemma = self.__leamatization(text_not_digit)
        return text_lemma

    def remove_ascii(self, text):
        logging.debug("Remove ascii")
        return "".join([word for word in text if ord(word) < 128])
