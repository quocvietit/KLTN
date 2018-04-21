"""
@name: test_lemmatization_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from data_analysis.service.lemmatization_service import LemmatizationService
import re
from nltk import pos_tag, word_tokenize



lemma = LemmatizationService()
text = "include and is includes included, horsing, lovely"
print pos_tag(word_tokenize(text))
text_clean = lemma.start(text)
print(text_clean)