"""
@name: test_remove_digit_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from data_analysis.service.remove_digit_service import RemoveDigitService

rm = RemoveDigitService()
text = "123 this is text remove service"
print rm.start(text)