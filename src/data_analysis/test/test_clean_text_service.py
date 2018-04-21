"""
@name: test_clean_text_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import sys
from data_analysis import setting

reload(sys)
sys.setdefaultencoding('utf8')

from data_analysis.service.clean_text_service import CleanTextService

clean = CleanTextService()
text = "This is numbers! 123 is a number?? Hello my bag it is on the desk"
text_clean = clean.start(text)
print (text_clean)
print setting.DATA