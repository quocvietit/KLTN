"""
@name: remove_digit_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import logging
import re

class RemoveDigitService:
    def __init__(self):
        pass

    def start(self, text):
        logging.debug("Remove digit")
        text_clean = re.sub(r"\d+", "", text)
        return text_clean
