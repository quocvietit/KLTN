"""
@name: date_string
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 22, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import datetime

def get_version():
    date = datetime.datetime.now()
    day = str(date.day) if date.day >= 10 else "0" + str(date.day)
    month = str(date.month) if date.month >= 10 else "0" + str(date.month)
    year = str(date.year)

    return day + month + year