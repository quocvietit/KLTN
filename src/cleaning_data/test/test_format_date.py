"""
@name: test_format_date
@author: Vuong Quoc Viet
@version: 1.0
@since: Mar 03, 2018
"""
import datetime
import dateutil.parser

date = datetime.datetime.strptime('2012-05-29T19:30:03.283Z', '%Y-%m-%dT%H:%M:%S.%fZ')
print date.second
date = dateutil.parser.parse('2014-05-18T12:19:24+04:00')
print date.second



