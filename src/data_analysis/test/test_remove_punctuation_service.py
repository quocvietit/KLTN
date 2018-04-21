"""
@name: test_remove_punctuation_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from data_analysis.service.remove_punctuation_service import RemovePunctuationService

rm = RemovePunctuationService()
text = 'This is a bag of word! How to remove stop words?'
text_clean = rm.remove_punctuation(text)
print(text_clean)
