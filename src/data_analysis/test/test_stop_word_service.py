"""
@name: test_stop_word_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import sys
from data_analysis.service.stop_word_service import StopWordService

reload(sys)
sys.setdefaultencoding('utf8')

text = 'This is a bag of word! How to remove stop words?'
stop_word_service = StopWordService("../data", "english")
text_clean = stop_word_service.remove_stop_words(text)
print(text_clean)