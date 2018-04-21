"""
@name: lemmatization_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import logging
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import pos_tag, word_tokenize


class LemmatizationService:
    def __init__(self):
        self.__lemma = WordNetLemmatizer()

    def start(self, text):
        logging.debug("Lemmatization text")
        normalized = []

        for word, tag in pos_tag(word_tokenize(text)):
            wntag = tag[0].lower()
            wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
            normalized.append(self.__lemma.lemmatize(word, wntag) if wntag else word)

        return normalized
